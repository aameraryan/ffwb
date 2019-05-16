from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, DeliveryAddress
from django.http import Http404
import datetime


def create(request):
    cart = request.user.cart_set.get(active=True)
    try:
        if request.method == "POST":
            delivery_address_id = request.POST['delivery_address_id']
            delivery_address = get_object_or_404(DeliveryAddress, id=delivery_address_id)
            order = Order.objects.create(cart=cart, total_amount=cart.total, delivery_before=datetime.date.today()+datetime.timedelta(days=3), delivery_address=delivery_address)
            return redirect('order:created', order_id=order.id)
        else:
            raise Http404
    except cart.DoesNotExist:
        raise Http404('No Cart Found')


def created(request, order_id):
    order = get_object_or_404(Order, id=order_id, cart__user=request.user)
    return render(request, 'order/created.html', {'order': order})
