from django import forms

from .models import Product, Tag

class TagChoiceField(forms.ModelChoiceField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('empty_label', 'Any')
        super(TagChoiceField, self).__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        return obj.value

class FilterForm(forms.Form):
    color = forms.ChoiceField(choices=Product.COLOR_CHOICES)


class ShirtFilterForm(forms.Form):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(ShirtFilterForm, self).__init__(*args, **kwargs)

    color = TagChoiceField(queryset=Tag.objects.filter(name='color'))
    use_type = TagChoiceField(queryset=Tag.objects.filter(category__name='t-shirts', name='type'))
    style = TagChoiceField(queryset=Tag.objects.filter(category__name='t-shirts', name='style'))
    fit = TagChoiceField(queryset=Tag.objects.filter(category__name='t-shirts', name='fit'))


class LongSleeveFilterForm(forms.Form):
    color = TagChoiceField(queryset=Tag.objects.filter(name='color'))
    use_type = TagChoiceField(queryset=Tag.objects.filter(category__name='long-sleeves shirts', name='type'))
    style = TagChoiceField(queryset=Tag.objects.filter(category__name='long-sleeves shirts', name='style'))
    fit = TagChoiceField(queryset=Tag.objects.filter(category__name='long-sleeves shirts', name='fit'))
    pattern = TagChoiceField(queryset=Tag.objects.filter(category__name='long-sleeves shirts', name='pattern'))


class ShortsFilterForm(forms.Form):
    color = TagChoiceField(queryset=Tag.objects.filter(name='color'))
    use_type = TagChoiceField(queryset=Tag.objects.filter(category__name='shorts', name='type'))
    length = TagChoiceField(queryset=Tag.objects.filter(category__name='shorts', name='length'))
    pattern = TagChoiceField(queryset=Tag.objects.filter(category__name='shorts', name='pattern'))


class PantsFilterForm(forms.Form):
    color = TagChoiceField(queryset=Tag.objects.filter(name='color'))
    use_type = TagChoiceField(queryset=Tag.objects.filter(category__name='pants', name='type')) 
    fit = TagChoiceField(queryset=Tag.objects.filter(category__name='pants', name='fit'))


class ShoesFilterForm(forms.Form):
    color = TagChoiceField(queryset=Tag.objects.filter(name='color'))
    use_type = TagChoiceField(queryset=Tag.objects.filter(category__name='shoes', name='type'))
    

class HatsFilterForm(forms.Form):
    color = TagChoiceField(queryset=Tag.objects.filter(name='color'))
    style = TagChoiceField(queryset=Tag.objects.filter(category__name='hats', name='style'))
