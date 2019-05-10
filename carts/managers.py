from django.db import models
from portal.models import Product
from django.conf import settings


class CartManager(models.Manager):

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)



