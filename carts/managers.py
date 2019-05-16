from django.db import models
from products.models import Product
from django.conf import settings


class CartManager(models.Manager):

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

    def get_or_new_by_user(self, user_id):
        cart = self.get_or_create(user_id=user_id)[0]
        return cart

    def get_or_new_by_id(self, cart_id):
        cart = self.model.objects.get_or_create(id=cart_id)[0]
        return cart

    def get_request_cart(self, request):
        if request.user.is_authenticated:
            cart = self.get_or_new_by_user(user_id=request.user.id)
        else:
            if 'cart_id' in request.session:
                cart = self.get_or_new_by_id(cart_id=request.session['cart_id'])
            else:
                cart = self.create()
                request.session['cart_id'] = cart.id
        return cart

