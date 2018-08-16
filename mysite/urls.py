from django.conf.urls import  url
from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url('elements/', views.elements, name='elements'),
    url('generic/', views.generic, name='generic'),
]
