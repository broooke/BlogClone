from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm, SignUpForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as dj_login
from django.contrib import messages

# Create your views here.

def home(request):
	posts = Post.objects.all()
	print(request.user.username)
	context = {'posts':posts}
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
	comments = Comment.objects.filter(post=post)
	context = {'post':post,'comments':comments}
	return render(request, 'post_des.html', context)

def comment(request,post_id):
	post = get_object_or_404(Post, id=post_id)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('description', post_id=post_id)
	else:
		form = CommentForm()
	context = {'post':post,'form':form}
	return render(request, 'comment.html', context)

def approved(request, post_id):
	post = Post.objects.get(id=post_id)
	post.posted()
	return redirect('description', post_id=post_id)

def approved_comment(request, post_id, comment_id):
	comment = Comment.objects.get(id=comment_id)
	comment.approved_comment()
	return redirect('description', post_id=post_id)

def drafts(request):
	posts = Post.objects.filter(date_posted=None)
	context = {'posts':posts}
	return render(request,'drafts.html',context)

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = SignUpForm()
	context = {'form':form}
	return render(request,'signup.html', context)

def login(request):
	form = AuthenticationForm()
	messages = None
	if request.method=='POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				dj_login(request,user)
				return redirect('home')
			else:
				messages=messages.add_message(request, messages.ERROR, 'Hello world.')
	context={'form':form,'messages':messages}
	return render(request,'login.html',context)

def logoutt(request):
	logout(request)
	return redirect('login')

def edit(request, post_id):
	post = Post.objects.get(id=post_id)
	form = PostForm(instance=post)
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('description', post_id=post_id)

	context = {'form':form}
	return render(request,'add_post.html', context)

def delete(request,post_id):
	post = get_object_or_404(Post,id=post_id)
	if request.method=='POST':
		post.delete()
		return redirect('home')
	return render(request,'confirm_delete.html') 

def delete_comment(request,post_id,comment_id):
	comment = get_object_or_404(Comment,id=comment_id)
	comment.delete()
	return redirect('description', post_id=post_id)





