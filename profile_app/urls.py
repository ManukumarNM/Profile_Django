from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #main page
    path('contact', views.contact_view, name='contact'), #contact page
    ]