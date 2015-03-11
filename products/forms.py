from django import forms

from .models import Product, Tag

class FilterForm(forms.Form):
    color = forms.ChoiceField(choices=Product.COLOR_CHOICES)

class ShirtFilterForm(forms.Form):
    style = forms.ModelChoiceField(queryset=Tag.objects.filter(name='style'))
    fit = forms.ModelChoiceField(queryset=Tag.objects.filter(name='fit'))
