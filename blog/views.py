from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse

# Create your views here.

def home(request):
	posts = Post.objects.all()
	com = len(posts)
	context = {'posts':posts,'com':com}
	return render(request,'home.html', context)

def add_post(request):
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			print(form.errors)
			return redirect('add_post')

	context = {'form':form}
	return render(request,'add_post.html', context)

def description(request, post_id):
	post = Post.objects.get(id=post_id)
	context = {'post':post}
	return render(request, 'post_des.html', context)

def comment(request,post_id):
	post = Post.objects.get(id=post_id)
	context = {'post':post}
	return render(request, 'comment.html', context)

