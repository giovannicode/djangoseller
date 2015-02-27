from django import forms
from django.db import transaction, IntegrityError
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib import messages

from braces.views import AnonymousRequiredMixin
from users.models import User
from users.forms import UserCreateForm
from carts.models import Cart


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    success_url = 'main:index'

    def form_valid(self, form): 
        try:
            with transaction.atomic():
                cart = Cart.objects.create()
                user = form.save(commit=False)
                user.cart = cart
                user.save()
               
        except IntegrityError:
            messages.add_message(
                self.request,
                messages.INFO,
                'I\'m sorry an unkown error occured'
            )
   
        user = authenticate(
            username=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password1')
        )
        login(self.request, user)
        return redirect('main:index')


class UserLoginView(AnonymousRequiredMixin, FormView):
    authenticated_redirect_url = u"/"
    template_name = 'users/login.html'
    form_class = AuthenticationForm
  
    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('main:index')


class ForgotPasswordView(FormView):
    template_name = 'users/forgot_password.html'
    form_class = PassordResetForm


def signout(request):
    logout(request)
    return redirect('main:index')
