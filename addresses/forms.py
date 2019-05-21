from .models import DeliveryAddress
from django import forms


class DeliveryAddressAddForm(forms.ModelForm):

    class Meta:
        model = DeliveryAddress
        fields = ('address_line_1', 'address_line_2', 'locality', 'address_type', 'contact_no')