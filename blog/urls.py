from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('description/<int:post_id>/', views.description , name='description'),
    path('description/<int:post_id>/comment/', views.comment , name='comment'),
    path('description/<int:post_id>/approved/', views.approved, name='approved'),
    path('description/<int:post_id>/approved_comment/<int:comment_id>/', views.approved_comment, name='approved_comment'),
    path('drafts/', views.drafts, name='drafts'),
    path('account/signup', views.signup, name='signup'),
]