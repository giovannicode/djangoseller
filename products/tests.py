from django.test import TestCase
from .models import Product

class ProductTests(TestCase):

    def test_create_product(self):
        self.asserRaises(IntegrityError, Product, name='seven')
