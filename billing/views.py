from decimal import Decimal

import stripe

from django.db import transaction, IntegrityError
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.views.generic import CreateView

from orders.models import Address, Order
from payments.models import Payment

stripe.api_key = "sk_test_w96KeQLCTh23810DSE2ykwIt"

class BillingView(CreateView):
    model = Address 
    template_name = 'billing/index.html'
    total = 0

    def get_context_data(self, **kwargs):
        context = super(BillingView, self).get_context_data(**kwargs)
        cart = self.request.user.cart
        for item in cart.cartitem_set.all():
            self.total += item.product.price 
        context['total'] = str(self.total)
        self.request['total'] = str(self.total)
        return context

    def form_valid(self, form):
        try:
            with transaction.atomic():
	        token = self.request.POST["stripeToken"]
		self.total = 5
		
		user = self.request.user
		email = user.email
		payment = Payment.objects.create(total=Decimal(self.total))
		address = form.save()

		order = Order.objects.create(
                            user=user, 
                            email=user.email, 
                            payment=payment, 
                            address=address
                        )
       
		charge = stripe.Charge.create(
		# Stripe works in cents instead of dollars.
		# Multiply price by 100 to convert to cents  
		             amount = int(self.total*100),
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
                str(err) + str(int(self.total*100))
            )
            return redirect('billing:index') 

	mssg = "Order ID: " + str(order.id) + "\n"
	mssg += "Total Charges: " + str(order.payment.total) 

	send_mail(
	    'Order Information',
	    mssg,
	    'support@seller.org',
	    ['***REMOVED***'],
	    fail_silently=False
	)
	messages.add_message(
	    self.request, 
	    messages.INFO, 
	    'Your Payment was processed successfully. A confirmation email has been sent to \
            ***REMOVED***'
        )
 
        return redirect('main:index')
