from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Product


class HomeView(TemplateView):
    template_name = 'portal/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_products'] = Product.objects.new_products()
        context['preferred_products'] = Product.objects.preferred_products()
        return context


class ProductDetailView(DetailView):
    template_name = 'portal/product_detail.html'
    pk_url_kwarg = "product_id"
    context_object_name = 'product'

    model = Product

    def get_object(self, queryset=None):
        return super().get_object()


    # def get_context_object_name(self, obj):
    #     return



#
# def home(request):
#     context = {
#         'new_products': Product.objects.new_products(),
#         'preferred_products': Product.objects.preferred_products(),
#         'active_products': Product.objects.active_products(),
#     }
#     return render(request, 'portal/home.html', context)
