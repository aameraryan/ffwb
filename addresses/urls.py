from django.conf.urls import url
from . import views

app_name = 'addresses'


urlpatterns = [
    url(r'^add/$', views.add, name='add'),

]
