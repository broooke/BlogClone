from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	text = models.TextField(blank=True)
	name = models.CharField(max_length=30)
	date_created = models.DateTimeField(default=timezone.now)
	date_posted = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.name

	def posted(self):
		self.date_posted=timezone.now()
		self.save()

	def count_comments(self):
		return self.comments.filter(approved=True)



class Comment(models.Model):
	post = models.ForeignKey('blog.Post',on_delete=models.CASCADE, related_name='comments')
	author = models.CharField(max_length=50)
	text = models.TextField(blank=True)
	date_created = models.DateTimeField(default=timezone.now)
	approved = models.BooleanField(default=False)

	def __str__(self):
		return self.author

	def approved_comment(self):
		self.approved=True
		self.save()



	