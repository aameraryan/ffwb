from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'portal'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^login/$', LoginView.as_view(template_name='portal/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='portal/logout.html'), name='logout'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),

    url(r'^products/detail/(?P<product_id>[0-9]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^products/list/$', views.ProductListView.as_view(), name='product_list'),

    url(r'^about_us/$', views.AboutUsView.as_view(), name='about_us'),

    # url(r'^$', views.home, name='home'),

]