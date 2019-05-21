from django import forms
from products.models import Product
import django_filters


class ProductFilter(django_filters.FilterSet):

    price = django_filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['categories', 'price', 'sizes', 'colors', 'current_ocassion']
