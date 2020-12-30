from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.todo, name='todo'),
    path('updatetodo/<str:pk>/', views.update_todo, name='updatetodo')
    ]