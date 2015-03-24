from django.db import models
from django.core.urlresolvers import reverse
from categories.models import Category

class Tag(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length='30')
    value = models.CharField(max_length='30')

    def __unicode__(self):
        return '[' + self.category.name + '] - ' + self.name + ': ' + self.value


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=14, decimal_places=2)
    qty = models.PositiveIntegerField()

    COLOR_CHOICES = (
        ('red', 'red'),
        ('orange', 'orange'),
        ('yellow', 'yellow'),
        ('green', 'green'),
        ('cyan', 'cyan'),
        ('blue', 'blue'), 
        ('purple', 'purple'),
        ('pink', 'pink'),
        ('brown', 'brown'),
        ('gold', 'gold'),
        ('black', 'black'),
        ('gray', 'gray'),
        ('white', 'white')
    )
    color = models.CharField(max_length=30, choices=COLOR_CHOICES) 
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
   
    class Meta:
        ordering = ['price']
    
    def get_absolute_url(self):
        return reverse('products:detail', args=[str(self.id)])

    def __unicode__(self):
        return self.name
