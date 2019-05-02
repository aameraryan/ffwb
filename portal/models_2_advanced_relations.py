from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=32)
    abbrevation = models.CharField(max_length=8)
    length = models.CharField(max_length=16)
    unit = models.CharField(max_length=16)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=32)
    abbrevation = models.CharField(max_length=8)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name


class PhotoPosition(models.Model):
    name = models.CharField(max_length=32)
    abbrevation = models.CharField(max_length=8)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProductPhoto(models.Model):
    photo = models.ImageField(upload_to='products/product_photos/')
    position = models.ForeignKey(PhotoPosition, on_delete=models.PROTECT)
    product_choice = models.ForeignKey('ProductChoice', on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.position, self.product_choice)


class Product(models.Model):
    name = models.CharField(max_length=20)
    details = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6)
    actual_price = models.DecimalField(max_digits=6)
    sizes = models.ManyToManyField(Size)

    def __str__(self):
        return self.name


class ProductChoice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.product, self.color)
