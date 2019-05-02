from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'portal'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^products/detail/(?P<product_id>[0-9]+)/$', views.ProductDetailView.as_view(), name='product_detail')
    # url(r'^$', views.home, name='home'),

]