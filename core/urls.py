from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('edit/', views.edit, name="edit"),
    path('word/', views.word, name="word"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('contact/', views.contact, name="contact"),
]
