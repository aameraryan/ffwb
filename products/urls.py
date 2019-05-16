from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'products'

urlpatterns = [
    url(r'^detail/(?P<product_id>[0-9]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^list/$', views.ProductListView.as_view(), name='product_list'),
]