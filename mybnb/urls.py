from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('home/', views.home, name='Home')
]