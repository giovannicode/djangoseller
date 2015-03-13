from django.test import TestCase, Client
from users.models import UserCreateForm

class UserTests(TestCase):
     def test_UserCreateForm_invalid_inputs(self): 
         form_data = {
             'username': 'crazycat@giovannicode.com', 
             'password': 'password5',
         }
         form = UserCreateForm(data=form_data)         
         self.assertEqual(form.is_invalid(), True) 
