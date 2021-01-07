from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm, SignUpForm
from django.http import HttpResponse

# Create your views here.

def home(request):
	posts = Post.objects.all()
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
	context = {'post':post,'comments':comments, 'len_comments':len_comments}
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


