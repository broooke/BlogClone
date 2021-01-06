from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
]