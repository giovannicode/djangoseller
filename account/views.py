from django import forms
from django.db import transaction, IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView

from users.models import User
from users.forms import UserCreateForm
from carts.models import Cart

from django.contrib import messages

class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'account/user_form.html'
    success_url = 'profiles:index'

    def form_valid(self, form): 
        try:
            with transaction.atomic():
                user = form.save()
                cart = Cart.objects.create(user=user)
                user = authenticate(
                    username=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password')
                )
                login(self.request, user)
                return redirect(self.success_url)
               
        except IntegrityError:
            messages.add_message(
                self.request,
                messages.INFO,
                'I\'m sorry an unkown error occured'
            )
        return reverse('main:index')