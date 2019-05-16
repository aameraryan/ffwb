from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.utils import timezone

USER_MODEL = settings.AUTH_USER_MODEL


class DeliveryAddress(models.Model):

    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=264)
    address_line_2 = models.CharField(max_length=264)
    address_line_3 = models.CharField(max_length=264)

    address_type = models.CharField(max_length=32, default='Home')
    city = models.CharField(max_length=32, default='Pune')

    contact_no = models.CharField(max_length=13)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.get_headline

    @property
    def get_headline(self):
        return self.address_line_1


class OrderManager(models.Manager):

    def place_order(self, **kwargs):
        order = self.create(**kwargs)
        order.cart.make_ordered()
        return order


class Order(models.Model):

    ORDER_STATUS_CHOICES = (('PL', "Placed"), ('PK', "Packed"), ("SH", "Shipped"))

    cart = models.OneToOneField('carts.Cart', on_delete=models.SET_NULL, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    delivery_amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_type = models.CharField(max_length=3, default='COD')
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.PROTECT)

    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=ORDER_STATUS_CHOICES, default="PL")
    delivery_before = models.DateField(default=timezone.now()+timezone.timedelta(days=5))
    deliverd_on = models.DateTimeField(blank=True, null=True)

    delivery_man = models.ForeignKey('DeliveryMan', on_delete=models.PROTECT, blank=True, null=True)

    details = models.TextField(blank=True)

    objects = OrderManager()

    def __str__(self):
        return str(self.id)


def assign_total_amount(sender, instance, *args, **kwargs):
    if not instance.total_amount:
        instance.total_amount = instance.cart.total + instance.delivery_amount
        instance.save()


post_save.connect(assign_total_amount, sender=Order)


class DeliveryMan(models.Model):
    name = models.CharField(max_length=32)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name
