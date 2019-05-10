from django.shortcuts import render
from .models import Cart


def home(request):
    cart = Cart.objects.get(user=request.user)
    product_entries = cart.productentry_set.all()
    return render(request, 'cart/home.html', {'cart': cart})

# def home(request):
#     cart_id = request.session.get('cart_id', None)
#     qs = Cart.objects.filter(id=cart_id)
#     if qs.exists():
#         cart = qs.first()
#         if request.user.is_authenticated and cart.user is None:
#             cart.user = request.user
#             cart.save()
#     else:
#         cart = Cart.objects.new(user=request.user)
#         request.session['cart_id'] = cart.id
#     return render(request, 'cart/home.html', {'cart': cart})
