from django.db import models
from django.conf import settings

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
    payment = models.OneToOneField(Payment)
    address = models.OneToOneField(Address)


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    qty = models.PositiveIntegerField() 
