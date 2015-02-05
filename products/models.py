from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=14, decimal_places=2)
    qty = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name
