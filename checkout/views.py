from decimal import Decimal

import stripe

from django.db import transaction
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic import FormView

from braces.views import UserPassesTestMixin

from carts.models import Cart
from orders.models import Address, Order, OrderItem
from payments.models import Payment
from .forms import CheckoutForm

stripe.api_key = "sk_test_w96KeQLCTh23810DSE2ykwIt"

class CheckoutView(UserPassesTestMixin, FormView):
    template_name = 'checkout/index.html'
    form_class = CheckoutForm
    login_url = '/'
     
    def test_func(self, user):
        if user.is_authenticated():
            return user.cart.cartitem_set.exists()
        else:
            try:
                self.request.session.modified = True
                cart = Cart.objects.get(session_key=self.request.session.session_key)
            except Cart.DoesNotExist:
                cart = Cart.objects.create(session_key=self.request.session.session_key)
            return cart.cartitem_set.exists()       

    def get_form(self, form_class):
        return form_class(self.request.user, **self.get_form_kwargs())

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            cart = self.request.user.cart
        else:
           cart = Cart.objects.get(session_key=self.request.session.session_key) 
        total = 0
        for item in cart.cartitem_set.all():
            total += item.product.price * item.qty 
        context['total'] = str(total)
        self.request.session['total'] = str(total)
        return context

    def form_valid(self, form):
        try:
            with transaction.atomic():
	        token = self.request.POST["stripeToken"]
		total = self.request.session['total']
		user = self.request.user

                if user.is_authenticated():
		    email = user.email
                    first_name = user.first_name
                    last_name = user.last_name
                    cart = user.cart
                else:
                    user = None
                    email = form.cleaned_data.get('email')
                    first_name = form.cleaned_data.get('first_name')
                    last_name = form.cleaned_data.get('last_name')
          
		payment = Payment.objects.create(total=Decimal(total))
		address = form.save()

		order = Order.objects.create(
                    user=user, 
                    email=email, 
                    payment=payment, 
                    address=address
                )
                if self.request.user.is_authenticated(): 
                    cart = self.request.user.cart
                else:
                    cart = Cart.objects.get(session_key=self.request.session.session_key)
                for cartitem in cart.cartitem_set.all():
                    orderitem = OrderItem.objects.create(
                        order=order,
                        product=cartitem.product,
                        title=cartitem.product.name,
                        price=cartitem.product.price,
                        qty=cartitem.qty
                    )
                cart.cartitem_set.all().delete()
       
		charge = stripe.Charge.create(
		# Stripe works in cents instead of dollars.
		# Multiply price by 100 to convert to cents  
		    amount = int(Decimal(total)*100),
		    currency="usd",
		    card = token,
		    description="New Order"
		)             
        
        except stripe.error.StripeError, e:            
            body = e.json_body
            err  = body['error']
            messages.add_message(
                self.request, 
                messages.INFO, 
                err
            )
            return redirect('billing:index') 

        html_mssg = render_to_string(
            'emails/order_confirmation.html', 
            { 
                'name': first_name + " " + last_name,
                'order': order,
            }
        )

	send_mail(
	    'Order Information',
	    html_mssg,
	    'support@seller.org',
	    recipient_list=['campusgino@gmail.com'],
	    fail_silently=False,
            html_message=html_mssg
	)
	messages.add_message(
	    self.request, 
	    messages.INFO, 
	    'Your Payment was processed successfully. A confirmation email has been sent to \
            campusgino@gmail.com'
        )

        return redirect('main:index')
