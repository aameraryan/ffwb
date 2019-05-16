from django import forms
from .models import Cart, CartItem


class CartUpdateView(forms.ModelForm):

    class Meta:
        model = Cart
        fields = ('product', 'quantity')
