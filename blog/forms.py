from django import forms
from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
	class Meta:
		model=Post
		fields=('author','name','text')

class CommentForm(ModelForm):
	class Meta:
		model=Comment
		fields=('author','text')


		