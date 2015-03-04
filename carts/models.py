from django.db import models
from django.conf import settings

from products.models import Product

class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True, null=True)

    def __unicode__(self):
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    qty = models.PositiveIntegerField() 
