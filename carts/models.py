from django.db import models
from django.conf import settings
from .managers import CartManager
from products.models import Product
from django.db.models.signals import pre_save, post_save
from django.http import Http404

USER_MODEL = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    # products = models.ManyToManyField('products.Product')

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    ordered = models.BooleanField(default=False)
    ordered_on = models.DateTimeField(blank=True, null=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


class Entry(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} X {} = {}".format(self.product.name, self.price, self.quantity, self.amount)

    def update_quantity(self, number):
        if not number.isdigit() or (self.quantity + int(number) < 0):
            raise Http404('Invalid Quantity')
        else:
            self.quantity += int(number)
            print(self.quantity)
            self.save()


def add_amount(sender, instance, *args, **kwargs):
    if instance.amount != (instance.price*instance.quantity):
        instance.amount = instance.price*instance.quantity
        instance.save()


post_save.connect(add_amount, sender=Entry)
