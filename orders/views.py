from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from django.http import Http404
import datetime
from carts.models import Cart, Entry
from products.models import Product
from django.contrib import messages
from . import alert_messages
import decimal
from addresses.forms import DeliveryAddressAddForm
from addresses.models import DeliveryAddress


def checkout(request):
    cart = Cart.objects.get_request_cart(request)
    if cart.is_non_empty:
        addresses = request.user.deliveryaddress_set.all()
        return render(request, 'order/checkout.html', {'cart': cart, 'addresses': addresses, 'addresss_add_form': DeliveryAddressAddForm()})
    raise Http404('Bad Request')


def create(request):
    if request.method == "POST":
        cart = Cart.objects.get_request_cart(request)
        if cart.is_non_empty:
            post_dict = request.POST
            delivery_address = get_object_or_404(request.user.deliveryaddress_set, id=post_dict['delivery_address'])
            delivery_amount = decimal.Decimal(100.00)
            order = Order.objects.place_order(cart=cart, delivery_amount=delivery_amount, delivery_address=delivery_address,
                                              total_amount=cart.total+delivery_amount)
            messages.success(request, alert_messages.ORDER_PLACED_MESSAGE)
            return redirect('orders:created', order_id=order.id)
    raise Http404('Bad Request')


def created(request, order_id):
    order = get_object_or_404(Order, id=order_id, cart__user=request.user)
    return render(request, 'order/created.html', {'order': order})


