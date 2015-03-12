from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='gio shirt', description='cool shirt', picture=)    

    def test_create_product(self):
        product = Products.objects.get(name='cup')
        self.assertEqual(product.name, 'cup')
