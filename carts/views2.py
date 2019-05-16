from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from django.contrib import messages
from . import alert_messages
from products.models import Product
from django.http import Http404


def home(request):
    cart = Cart.objects.get_request_cart(request=request)
    return render(request, 'cart/home.html', {'cart': cart})


def update(request):
    if request.method == "POST":
        post_dict = request.POST
    else:
        return redirect('cart:home')


def add_product(request, product_id):
    cart = Cart.objects.get_request_cart(request)
    product = get_object_or_404(Product, id=product_id)
    if product not in cart.products.all():
        cart.product.add(product)
        messages.success(request, alert_messages.PRODUCT_ADDED_MESSAGE)
    else:
        messages.warning(request, alert_messages.PRODUCT_ALREADY_IN_CART)
        print(alert_messages.PRODUCT_ALREADY_IN_CART)
    return redirect('carts:home')


def remove_product(request, product_id):
    cart = Cart.objects.get_request_cart(request)
    product = get_object_or_404(cart.products.all(), id=product_id)
    cart.products.remove(product)
    messages.success(request, alert_messages.PRODUCT_REMOVED_MESSAGE)
    return redirect('carts:home')
