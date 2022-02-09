from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #main page
    path('contact', views.contact, name='contact'), #contact page
    ]