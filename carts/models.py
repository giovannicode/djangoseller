from django.db import models
from django.conf import settings

from products.models import Product

class Cart(models.Model):

    def __unicode__(self):
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    qty = models.PositiveIntegerField() 
