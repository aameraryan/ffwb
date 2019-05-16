from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Entry
from django.contrib import messages
from . import alert_messages
from products.models import Product
from django.http import Http404
from django.views.generic import UpdateView


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
    product_cart_item, is_created = Entry.objects.create_entry(product_id=product_id, price=product.price, cart=cart)
    if is_created:
        messages.success(request, alert_messages.PRODUCT_ADDED_MESSAGE)
    else:
        messages.warning(request, alert_messages.PRODUCT_ALREADY_IN_CART)
    return redirect('carts:home')


def remove_product(request, product_id):
    cart = Cart.objects.get_request_cart(request)
    product_cart_item = Entry.objects.remove_entry(product_id=product_id, cart=cart)
    messages.success(request, alert_messages.PRODUCT_REMOVED_MESSAGE)
    return redirect('carts:home')


def quantity_update(request, entry_id, number):
    cart = Cart.objects.get_request_cart(request)
    entry = get_object_or_404(Entry, id=entry_id, cart=cart)
    entry.update_quantity(number)
    entry.cart.save()
    return redirect('carts:home')

