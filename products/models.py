from django.db import models
from django.core.urlresolvers import reverse
from categories.models import Category

class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=14, decimal_places=2)
    qty = models.PositiveIntegerField()

    categories = models.ManyToManyField(Category)
   
    class Meta:
        ordering = ['price']
    
    def get_absolute_url(self):
        return reverse('products:detail', args=[str(self.id)])

    def __unicode__(self):
        return self.name
