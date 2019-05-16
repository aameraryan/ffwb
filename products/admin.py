from django.contrib import admin
from .models import Product, ProductPhoto, Category, Size, Color, PhotoPosition


admin.site.register(Size)
admin.site.register(Color)
admin.site.register(PhotoPosition)
admin.site.register(Category)
admin.site.register(ProductPhoto)


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'created_on', 'updated_on')

    inlines = (ProductPhotoInline, )


admin.site.register(Product, ProductAdmin)
