from django.contrib import admin
from .models import Order, DeliveryAddress, DeliveryMan

admin.site.register(Order)
admin.site.register(DeliveryAddress)
admin.site.register(DeliveryMan)
