from decimal import Decimal

import stripe

from django.db import transaction
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic import CreateView

from orders.models import Address, Order, OrderItem
from payments.models import Payment

stripe.api_key = "sk_test_w96KeQLCTh23810DSE2ykwIt"

class CheckoutView(CreateView):
    model = Address 
    template_name = 'checkout/index.html'

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        cart = self.request.user.cart
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
		email = user.email
		payment = Payment.objects.create(total=Decimal(total))
		address = form.save()

		order = Order.objects.create(
                    user=user, 
                    email=user.email, 
                    payment=payment, 
                    address=address
                )
   
                cart = self.request.user.cart
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
                'name': self.request.user.first_name + " " + self.request.user.last_name,
                'order': order,
            }
        )

	send_mail(
	    'Order Information',
	    html_mssg,
	    'support@seller.org',
	    recipient_list=['***REMOVED***'],
	    fail_silently=False,
            html_message=html_mssg
	)
	messages.add_message(
	    self.request, 
	    messages.INFO, 
	    'Your Payment was processed successfully. A confirmation email has been sent to \
            ***REMOVED***'
        )

        return redirect('main:index')
