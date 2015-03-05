from django import forms

from orders.models import Address

class CheckoutForm(forms.Form):
    
    # These fields correspond to the address model
    street = forms.CharField(max_length=60)
    city = forms.CharField(max_length=60)
    state = forms.CharField(max_length=2)
    zipcode = forms.CharField(max_length=5)

    def __init__(self, user, *args, **kwargs): 
        super(CheckoutForm, self).__init__(*args, **kwargs)
        # The email field will be conditional. It will depend on whether or not the user is logged in.
        if not user.is_authenticated():
            self.fields['email'] = forms.EmailField()

    def save(self):
        street = self.cleaned_data.get('street') 
        city = self.cleaned_data.get('city')
        state = self.cleaned_data.get('state')
        zipcode = self.cleaned_data.get('zipcode')

        address = Address.objects.create(
            street=street,
            city=city,
            state=state,
            zipcode=zipcode
        )
        return address 
