from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


class Locality(models.Model):
    name = models.CharField(max_length=128)
    coordinates = models.CharField(max_length=256, blank=True)
    delivery_charges = models.DecimalField(max_digits=7, decimal_places=2)
    city = models.CharField(max_length=128, default="Pune")

    def __str__(self):
        return self.name


class DeliveryAddress(models.Model):

    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    address_line_1 = models.CharField(verbose_name="Flat or builiding name", max_length=264)
    address_line_2 = models.CharField(verbose_name="Street Name", max_length=264)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)

    address_type = models.CharField(max_length=32, default='Home')

    contact_no = models.CharField(max_length=13)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.get_headline

    @property
    def get_headline(self):
        return self.address_line_1


