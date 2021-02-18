from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hom, name='home'),
    path('youtbdown/', views.youtbdown ,name= "youtbdown"),
    path('download/<res>', views.download ,name= "download"),
    
]
