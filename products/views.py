from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Product


class ProductDetailView(DetailView):
    template_name = 'products/detail.html'
    pk_url_kwarg = "product_id"
    context_object_name = 'product'

    model = Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'

