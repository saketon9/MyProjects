from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('index/', views.index, name='index'),
    path('FresherQuestion', views.fresherquestion, name='fresherQuestion'),
    path('Java', views.java, name='Java'),
    path('Cprogramming', views.cProgram, name='cprogramming'),
    path('PHP', views.php, name='PHP'),
    path('About', views.about, name='About'),
    path('Register', views.register, name='Register'),
    path('Login', views.login, name='Login'),
    path('Logout', views.logout, name='Logout'),
    path('comReview', views.comreview, name='comReview'),
    path('google', views.Google, name='google'),
    path('facebook', views.Facebook, name='facebook'),
    path('khoros', views.Khoros, name='khoros')

]