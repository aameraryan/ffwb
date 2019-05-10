from django.db import models
from django.conf import settings
from .managers import CartManager
from portal.models import Product
from django.db.models.signals import pre_save, post_save


USER_MODEL = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    ordered = models.BooleanField(default=False)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


class DeliveryMan(models.Model):
    name = models.CharField(max_length=32)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProductEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {} X {} = {}".format(self.product.name, self.price, self.quantity, self.amount)


def add_amount_to_product_entry(sender, instance, *args, **kwargs):
    if instance.amount != (instance.price*instance.quantity):
        instance.amount = instance.price*instance.quantity
        instance.save()


pre_save.connect(add_amount_to_product_entry, sender=ProductEntry)


class DeliveryAddress(models.Model):
    name = models.CharField(max_length=128)
    address_line_1 = models.CharField(max_length=264)
    address_line_2 = models.CharField(max_length=264)
    address_line_3 = models.CharField(max_length=264)

    address_type = models.CharField(max_length=32, default='Home')
    city = models.CharField(max_length=32, default='Pune')

    contact_no = models.CharField(max_length=13)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.PROTECT)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_type = models.CharField(max_length=3, default='COD')

    created_on = models.DateTimeField(auto_now_add=True)
    delivery_before = models.DateField()
    deliverd_on = models.DateTimeField(blank=True, null=True)

    delivery_man = models.ForeignKey(DeliveryMan, on_delete=models.PROTECT)

    details = models.TextField(blank=True)

    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)
