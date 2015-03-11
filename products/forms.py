from django import forms

from .models import Product, Tags

class FilterForm(forms.Form):
    color = forms.ChoiceField(choices=Product.COLOR_CHOICES)

class ShirtFilterForm(forms.Form):
    style = forms.ModelChoiceField(queryset=Tags.objects.filter(name='style')
    fit = forms.ModelChoiceField(queryset=Tags.objects.filter(name='fit')
