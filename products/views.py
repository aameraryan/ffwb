from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Product


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    pk_url_kwarg = "product_id"
    context_object_name = 'product'

    model = Product

    def get_object(self, queryset=None):
        return super().get_object()


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

