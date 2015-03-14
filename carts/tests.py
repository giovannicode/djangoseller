from django.contrib.auth import authenticate, login
from django.test import TestCase, RequestFactory
from users.models import User
from .views
               

class CartTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            first_name='Giovanni',
            last_name='Arroyo', 
            email='***REMOVED***',
            password='password'
        )

    def test_anonymous_user_cart_detail_view(self):
        response = self.client.get('/carts/detail')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_cart_detail_view(self):
        request.user = self.user
        request = self.factory.get('/carts/detail')
        response = 
        self.assertEqual(response.status_code, 200)

