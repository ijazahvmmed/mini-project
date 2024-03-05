from django.contrib import admin
from django.urls import path, include
from login import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.index, name="login"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('home', views.home, name="home"),
    path('about', views.about , name="about"),
]