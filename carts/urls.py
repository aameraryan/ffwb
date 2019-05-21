from django.conf.urls import url
from . import views

app_name = 'carts'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^add_product/(?P<product_id>[0-9]+)$', views.add_product, name='add_product'),
    url(r'^add_product/$', views.add_product, name='add_product'),
    url(r'^remove_product/(?P<product_id>[0-9]+)$', views.remove_product, name='remove_product'),

    url(r'^quantity/update/(?P<entry_id>[0-9]+)/(?P<number>[0-9]+)/$', views.quantity_update, name='quantity_update'),
    # url(r'^quantity/decrease/(?P<number>[0-9]+)$', views.quantity_decrease, name='quantity_decrease'),

]