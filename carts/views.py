from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Entry
from django.contrib import messages
from . import alert_messages
from products.models import Product
from django.http import Http404
from django.views.generic import UpdateView
from orders.models import Order
from lazysignup.decorators import allow_lazy_user
from django.http import HttpResponse, JsonResponse


def get_request_orders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(cart__user=request.user)
    else:
        cart = Cart.objects.get_request_cart(request=request)
        orders = Order.objects.filter(cart=cart)
    return orders


@allow_lazy_user
def home(request):
    cart = Cart.objects.get_request_cart(request=request)
    orders = get_request_orders(request)
    pending_orders = orders.exclude(status="DL")
    delivered_orders = orders.filter(status="DL")
    return render(request, 'cart/home.html', {'cart': cart, 'orders': orders,
                                              'pending_orders': pending_orders, 'delivered_orders': delivered_orders})


def update(request):
    if request.method == "POST":
        post_dict = request.POST
    else:
        return redirect('cart:home')

#   AJAX REQUEST


def add_product(request):
    if request.method == "GET":
        print(request.GET)
        cart = Cart.objects.get_request_cart(request)
        product = get_object_or_404(Product, id=request.GET['product_id'])
        product_cart_item, is_created = Entry.objects.create_entry(product=product, price=product.price,
                                                                   cart=cart)
        if is_created:
            message = alert_messages.PRODUCT_ADDED_MESSAGE
        else:
            message = alert_messages.PRODUCT_ALREADY_IN_CART
    else:
        message = "Not GET request"
    return JsonResponse({"message": message})


#   NON AJAX - REDIRECTS TO CART VIEW
#
# def add_product(request, product_id):
#     cart = Cart.objects.get_request_cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     product_cart_item, is_created = Entry.objects.create_entry(product_id=product_id, price=product.price, cart=cart)
#     if is_created:
#         messages.success(request, alert_messages.PRODUCT_ADDED_MESSAGE)
#     else:
#         messages.warning(request, alert_messages.PRODUCT_ALREADY_IN_CART)
#     return redirect('carts:home')


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

