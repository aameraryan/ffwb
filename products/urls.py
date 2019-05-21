from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .filters import ProductFilter
from django_filters.views import FilterView

app_name = 'products'

urlpatterns = [
    url(r'^detail/(?P<product_id>[0-9]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^list/$', views.ProductListView.as_view(), name='product_list'),
    url(r'^search/$', FilterView.as_view(filterset_class=ProductFilter,
                                         template_name='products/search.html'), name='search')
]

