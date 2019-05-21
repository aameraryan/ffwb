from django.db import models
from .managers import ProductManager
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


class Size(models.Model):
    name = models.CharField(max_length=32)
    abbrevation = models.CharField(max_length=8)
    length = models.CharField(max_length=16)
    unit = models.CharField(max_length=16, default="Inch")
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @property
    def get_text(self):
        return self.abbrevation


class Color(models.Model):
    name = models.CharField(max_length=32)
    abbrevation = models.CharField(max_length=8)
    hex_code = models.CharField(max_length=7, default="#FF0000")
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @property
    def get_hex_code(self):
        return self.hex_code

    @property
    def get_text(self):
        return self.abbrevation


class PhotoPosition(models.Model):
    name = models.CharField(max_length=32)
    abbrevation = models.CharField(max_length=8)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @property
    def get_text(self):
        return self.abbrevation


class ProductPhoto(models.Model):
    photo = models.ImageField(upload_to='products/product_photos/')
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    position = models.ForeignKey(PhotoPosition, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    base_photo = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.position, self.product.name)

    @property
    def get_photo_url(self):
        return self.photo.url

    @property
    def get_position(self):
        return self.position.get_text


class Category(models.Model):
    name = models.CharField(max_length=16)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @property
    def get_text(self):
        return self.name


class Product(models.Model):

    PREFERENCE_CHOICES = ((1, 'Excellent'), (2, 'Very Good'), (3, 'Good'), (4, 'Average'))

    name = models.CharField(max_length=16)
    headline = models.CharField(max_length=48)
    details = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    actual_price = models.DecimalField(max_digits=6, decimal_places=2)
    sizes = models.ManyToManyField(Size)
    colors = models.ManyToManyField(Color)
    preference = models.PositiveSmallIntegerField(default=2, choices=PREFERENCE_CHOICES)

    current_ocassion = models.BooleanField(default=False)

    categories = models.ManyToManyField(Category)
    tag = models.CharField(max_length=5, blank=True)

    available_pieces = models.PositiveSmallIntegerField(default=100)
    out_of_stock = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return self.name

    @property
    def get_headline(self):
        return self.headline

    @property
    def get_base_photo_url(self):
        return self.productphoto_set.get(base_photo=True).photo.url

    @property
    def get_non_base_photos(self):
        return self.productphoto_set.filter(base_photo=False)

    @property
    def get_off_price(self):
        return self.price - self.actual_price

    @property
    def get_colors(self):
        return self.colors.all()

    @property
    def get_color_hex_codes(self):
        return self.colors.values_list('hex_code', flat=True)

    @property
    def get_color_names(self):
        return self.colors.values_list('name', flat=True)

    @property
    def get_size_names(self):
        return self.sizes.values_list('name', flat=True)

    @property
    def get_absolute_url(self):
        return reverse_lazy('products:product_detail', kwargs={'product_id': self.id})

    @property
    def get_add_to_cart_url(self):
        return reverse_lazy('carts:add_product', kwargs={'product_id': self.id})

    @property
    def get_remove_from_cart_url(self):
        return reverse_lazy('carts:remove_product', kwargs={'product_id': self.id})

    def clean(self):
        if self.productphoto_set.filter(base_photo=True).count() != 1:
            raise ValidationError("There should be exact 1 base photo")
