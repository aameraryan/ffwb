from .models import DeliveryAddress
from django import forms


class DeliveryAddressAddForm(forms.ModelForm):


    class Meta:
        model = DeliveryAddress
        fields = ('address_line_1', 'address_line_2', 'address_line_3', 'address_type', 'city', 'contact_no')