from django import forms

from .models import Product, Tag

class TagChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.value

class FilterForm(forms.Form):
    color = forms.ChoiceField(choices=Product.COLOR_CHOICES)

class ShirtFilterForm(forms.Form):
    color = TagChoiceField(queryset=Tag.objects.filter(name='color'))
    style = TagChoiceField(queryset=Tag.objects.filter(name='style'))
    fit = TagChoiceField(queryset=Tag.objects.filter(name='fit'))

class LongSleeveFilterForm(forms.Form):
    color = TagChoiceField(queryset=Tag.objects.filter(name='color'))
    style = TagChoiceField(queryset=Tag.objects.filter(name='style'))
    fit = TagChoiceField(queryset=Tag.objects.filter(name='fit'))
    pattern = TagChoiceField(queryset=Tag.objects.filter(name='pattern'))
