from django.db import models


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
    cart = models.OneToOneField('carts.Cart', on_delete=models.PROTECT)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_type = models.CharField(max_length=3, default='COD')

    created_on = models.DateTimeField(auto_now_add=True)
    delivery_before = models.DateField()
    deliverd_on = models.DateTimeField(blank=True, null=True)

    delivery_man = models.ForeignKey('DeliveryMan', on_delete=models.PROTECT)

    details = models.TextField(blank=True)

    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)


class DeliveryMan(models.Model):
    name = models.CharField(max_length=32)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name
