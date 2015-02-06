from django.db import models
from django.conf import settings

from products.models import Product

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)


class CartItem(models.Model):
    product = models.ForeignKey(Product)
    qty = models.PositiveIntegerField()
    
