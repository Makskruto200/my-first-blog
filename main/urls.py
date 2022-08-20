from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("create_user/", views.create_user, name='create_user'),
    path('login/', views.login, name='login'),



]
