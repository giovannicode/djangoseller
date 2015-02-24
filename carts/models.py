from django.db import models
from django.conf import settings

from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return str(self.user) + "'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    qty = models.PositiveIntegerField() 
