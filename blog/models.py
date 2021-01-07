from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	text = models.TextField(blank=True)
	name = models.CharField(max_length=30)
	date_created = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.name

class Comment(models.Model):
	post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)
	author = models.CharField(max_length=50)
	text = models.TextField(blank=True)
	date_created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.author

	def get_url(self):
		return reverse('description', args = [self.post_id])