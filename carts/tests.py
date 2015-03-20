from django.contrib.auth import authenticate, login
from django.test import TestCase, RequestFactory
from users.models import User
from .models import Cart
from .views import CartDetailView
               
class CartTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        # Create User with cart 
        cart = Cart.objects.create()
        self.user = User.objects.create_user(
            first_name='Giovanni',
            last_name='Arroyo', 
            email='campusgino@gmail.com',
            password='password',
        )
        self.user.cart = cart
        self.user.save()

    def test_anonymous_user_cart_detail_view(self):
        response = self.client.get('/carts/detail')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_cart_detail_view(self):
        request = self.factory.get('/carts/detail')
        request.user = self.user
        response = CartDetailView.as_view()(request) 
        self.assertEqual(response.status_code, 200)
