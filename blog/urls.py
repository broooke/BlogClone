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
    path('account/login', views.login, name='login'),
    path('account/logout', views.logoutt, name='logout'),
    path('description/<int:post_id>/edit/', views.edit, name='edit'),
    path('description/<int:post_id>/delete/', views.delete, name='delete'),
    path('description/<int:post_id>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]