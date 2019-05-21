from django.db import models
from products.models import Product
from django.conf import settings
from django.shortcuts import get_object_or_404
from lazysignup.decorators import allow_lazy_user


class CartManager(models.Manager):

    def get_or_new_by_user(self, user_id):
        cart = self.get_or_create(user_id=user_id, ordered=False)[0]
        return cart

    def get_request_cart(self, request):
        # cart = self.get_or_new_by_user(user_id=request.user.id)
        cart = self.get_or_create(user_id=request.user.id, ordered=False)[0]
        return cart


class EntryManager(models.Manager):

    def create_entry(self, **kwargs):
        entry, is_created = self.get_or_create(**kwargs)
        entry.cart.save()
        return entry, is_created

    def remove_entry(self, **kwargs):
        entry = get_object_or_404(self.model, **kwargs)
        entry.delete()
        kwargs['cart'].save()
