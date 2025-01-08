from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/',index.as_view(),name='home'),
    path('',Login.as_view(),name='login'),
    path('register/',Register.as_view(),name='register'),

 
]
