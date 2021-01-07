from django import forms
from django.forms import ModelForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(ModelForm):
	class Meta:
		model=Post
		fields=('author','name','text')

class CommentForm(ModelForm):
	class Meta:
		model=Comment
		fields=('author','text')

class SignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username','email','password1', 'password2')
		




		