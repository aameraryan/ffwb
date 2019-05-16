from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from products.models import Product
from django.contrib import messages
from .forms import RegisterForm


class RegisterView(TemplateView):

    template_name = 'portal/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegisterForm()
        return context


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'registered. now login')
            redirect('portal:login')
        else:
            form = RegisterForm()
    else:
        form = RegisterForm()
    return render(request, 'portal/login.html', {'form': form})


class HomeView(TemplateView):
    template_name = 'portal/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_products'] = Product.objects.new_products()
        context['preferred_products'] = Product.objects.preferred_products()
        return context


class AboutUsView(TemplateView):
    template_name = 'portal/about_us.html'


# def add_to_wish_list(request, product_id):
#     product = get

#
# def home(request):
#     context = {
#         'new_products': Product.objects.new_products(),
#         'preferred_products': Product.objects.preferred_products(),
#         'active_products': Product.objects.active_products(),
#     }
#     return render(request, 'portal/home.html', context)
