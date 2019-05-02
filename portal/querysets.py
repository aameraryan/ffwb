from django.db import models


class ProductQueryset(models.query.QuerySet):

    def avalaible_products(self):
        return self.filter(out_of_stock=False)

    def preferred_products(self):
        return self.order_by('-preference')

    def new_products(self):
        return self.order_by('-created_on')
