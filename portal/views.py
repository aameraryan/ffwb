from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView, FormView
from products.models import Product
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from carts.models import Cart
from lazysignup.decorators import allow_lazy_user

class RegisterView(FormView):

    template_name = 'portal/register.html'

    form_class = RegisterForm

    def form_valid(self, form):
        form.save()
        messages.info(self.request, "Thanks for registering. You are now logged in.")
        new_user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'],
                                )
        login(self.request, new_user)
        return redirect("portal:home")


class HomeView(TemplateView):
    template_name = 'portal/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_products'] = Product.objects.new_products()
        context['preferred_products'] = Product.objects.preferred_products()
        context['cart'] = Cart.objects.get_request_cart()
        return context


@allow_lazy_user
def home(request):
    context = {}
    context['new_products'] = Product.objects.new_products()
    context['preferred_products'] = Product.objects.preferred_products()
    context['cart'] = Cart.objects.get_request_cart(request)
    return render(request, "portal/home.html", context)


class AboutUsView(TemplateView):
    template_name = 'portal/about_us.html'


def contact(request):
    return render(request, "portal/contact.html")
