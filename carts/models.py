from django.db import models
from django.conf import settings
from .managers import CartManager, EntryManager
from products.models import Product
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.http import Http404
from django.utils import timezone
from django.db.models import Aggregate, Count, Sum

USER_MODEL = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)

    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    ordered = models.BooleanField(default=False)
    ordered_on = models.DateTimeField(blank=True, null=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    def make_ordered(self):
        self.ordered = True
        self.ordered_on = timezone.now()
        self.save()
        return self

    @property
    def is_non_empty(self):
        return self.entry_set.all()

    @property
    def get_entries(self):
        return self.entry_set.all()

    @property
    def get_total(self):
        return self.total


def upgrade_total(sender, instance, *args, **kwargs):
    total = instance.entry_set.all().aggregate(Sum('amount')).get('amount__sum', 0.00)
    total = 0.00 if total is None else total
    if instance.total != total:
        instance.total = total
        instance.save()


post_save.connect(upgrade_total, sender=Cart)


class Entry(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    color = models.ForeignKey("products.Color", on_delete=models.CASCADE)
    size = models.ForeignKey('products.Size', on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = EntryManager()

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
