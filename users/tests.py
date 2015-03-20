from django.test import TestCase, Client, RequestFactory
from users.models import User
from users.forms import UserCreateForm
from carts.models import Cart
from views import *

class UserCreateFormTests(TestCase):

    def test_UserCreateForm_missing_inputs(self): 
        form_data = {
            'username': 'crazycat@giovannicode.com', 
            'password': 'password5',
        }
        form = UserCreateForm(data=form_data)         
        self.assertEqual(form.is_valid(), False) 

    def test_UserCreateForm_invalid_email(self):
        response = self.client.post('/users/signup', {'email': 'campus'})
        self.assertFormError(response, 'form', 'email',  'Enter a valid email address.') 

    def test_UserCreateForm_non_identical_passwords(self):
        form_data = {
            'first_name': 'Giovanni',
            'last_name': 'Arroyo',
            'email': 'campusgino@gmail.com',
            'password1': 'password',
            'password2': 'differentpassword'
        }
        form = UserCreateForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_UserCreateForm_valid_inputs(self):
        form_data = {
            'first_name': 'Giovanni', 
            'last_name': 'Arroyo',
            'email': 'campusgino@gmail.com',
            'password1': 'password',
            'password2': 'password',
        }
        form = UserCreateForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_UserCreateForm_see_if_form_actually_created_user(self):
        form_data = {
            'first_name': 'Giovanni',
            'last_name': 'Arroyo',
            'email': 'campusgino@gmail.com',
            'password1': 'password',
            'password2': 'password'
        }
        form = UserCreateForm(data=form_data)
        form.save()
        self.assertEqual(User.objects.filter(email='campusgino@gmail.com').exists(), True)


class UserViewTests(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        cart = Cart.objects.create()
        self.user = User.objects.create_user(
            first_name='Giovanni',
            last_name='Arroyo',
            email='campusgino@gmail.com',
            password='password',
        )
        self.user.cart = cart
        self.user.save()

    def test_authenticated_user_redirects_when_visitin_login_view(self):        
        request = self.factory.get('/users/signin')
        request.user = self.user
        response = UserLoginView.as_view()(request)
        self.assertEqual(response.status_code, 302)
