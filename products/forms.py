from django import forms

from .models import Product

class FilterForm(forms.Form):
    color = forms.ChoiceField(choices=Product.COLOR_CHOICES)
