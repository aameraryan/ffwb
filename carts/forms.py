from django import forms
from .models import Cart, Entry


class CartUpdateView(forms.ModelForm):

    class Meta:
        model = Cart
        fields = ('entry', )
