from django.db import models
from django.conf import settings

from products.models import Product

class Review(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    RATING_CHOICES = (
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()   

    def __unicode__(self):
        return self.product.name + ", " + str(self.user) + ", " + str(self.rating)
