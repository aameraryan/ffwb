from django.db import models
from django.conf import settings

User_Model = settings.AUTH_USER_MODEL


class WhishList(models.Model):
    user = models.OneToOneField(User_Model, on_delete=models.CASCADE, blank=True, null=True)
    products = models.ManyToManyField('portal.Product')

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.get_products_count)

    @property
    def get_products_count(self):
        return self.products.all().count()


