from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^create/$', views.create, name='create'),
    url(r'^created/(?P<order_id>[0-9]+)/$', views.created, name='created'),
    url(r'^address/add/$', views.delivery_address_add, name='delivery_address_add'),

]