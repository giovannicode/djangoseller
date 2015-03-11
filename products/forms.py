from django import forms

from .models import Product, Tag

class TagChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return self.value

class FilterForm(forms.Form):
    color = forms.ChoiceField(choices=Product.COLOR_CHOICES)

class ShirtFilterForm(forms.Form):
    style = forms.TagChoiceField(queryset=Tag.objects.filter(name='style'))
    fit = forms.TagChoiceField(queryset=Tag.objects.filter(name='fit'))
