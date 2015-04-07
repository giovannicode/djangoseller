from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from products.models import Product
from payments.models import Payment


class Address(models.Model):
    street = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5) 

    def __unicode__(self):
        return "{street}, {city}, {state}, {zipcode}".format(
            street=self.street,
            city=self.city,
            state=self.state,
            zipcode=self.zipcode
        )


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    payment = models.OneToOneField(Payment)
    address = models.OneToOneField(Address)
    shipped = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('orders:detail', args=[str(self.id)])

    def __unicode__(self):
        return "Order ID: {id}, Email: {email}, Shipped: {shipped}"\
               .format(id=self.id, email=self.email, shipped=self.shipped)

    def save(self, *args,**kwargs):
        if self.pk is not None:
           orig = Order.objects.get(pk=self.pk)
           if orig.shipped == False and self.shipped == True:
               send_mail(
                   'Your order has been shipped',
                   'Hi ' + self.user.first_name + ', we though you\'d like to know that you order has been shipped',
                   'sales@djangoseller.com',
                   [self.email],
                   fail_silently=False
               )
        super(Order, self).save(*args, **kwargs)
                    

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    qty = models.PositiveIntegerField() 
