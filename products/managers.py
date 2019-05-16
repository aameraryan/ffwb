from django.db import models


class ProductQueryset(models.QuerySet):

    def avalaible_products(self):
        return self.filter(out_of_stock=False)

    def preferred_products(self):
        return self.order_by('-preference')

    def new_products(self):
        return self.order_by('-created_on')

    def active_products(self):
        return self.filter(active=True)


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQueryset(self.model, using=self.db)

    def available_products(self):
        return self.get_queryset().avalaible_products()

    def preferred_products(self):
        return self.get_queryset().preferred_products()

    def new_products(self):
        return self.get_queryset().new_products()

    def active_products(self):
        return self.get_queryset().active_products()
