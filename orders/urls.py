from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^create/$', views.create, name='create'),
    url(r'^created/(?P<order_id>[0-9]+)/$', views.created, name='created'),

]