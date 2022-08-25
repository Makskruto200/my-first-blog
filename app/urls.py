from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path("<int:pk>", views.AppsDetailView.as_view(), name='apps-detail'),
    path("comments_created/", views.comments_creade, name='comments_creade'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('add/', views.add, name='add'),
    path('update-app/', views.update_app, name='update-app'),
    path('update-applications/', views.update_applications, name='update-applications'),
    path('update-comment/', views.update_comment, name='update-comment'),
    path('delete-app/', views.delete_app, name='delete-app'),
    path('delete-applications/', views.delete_applications, name='delete-applications'),
    path('delete-comment/', views.delete_comment, name='delete-comment'),


]
