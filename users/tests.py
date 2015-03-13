from django.test import TestCase, Client
from users.models import Use:
from users.forms import UserCreateForm

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
            'email': '***REMOVED***',
            'password1': 'password',
            'password2': 'differentpassword'
        }
        form = UserCreateForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_UserCreateForm_valid_inputs(self):
        form_data = {
            'first_name': 'Giovanni', 
            'last_name': 'Arroyo',
            'email': '***REMOVED***',
            'password1': 'password',
            'password2': 'password',
        }
        form = UserCreateForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_UserCreateForm_see_if_form_actually_created_user(self):
        form_data = {
            'first_name': 'Giovanni',
            'last_name': 'Arroyo',
            'email': '***REMOVED***',
            'password1': 'password',
            'password2': 'password'
        }
        form = UserCreateForm(data=form_data)
        form.save()
        self.assertEqual(User.objects.filter(email='***REMOVED***').exists(), True)
