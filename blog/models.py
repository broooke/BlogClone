from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	text = RichTextField(blank=True, null=True)
	name = models.CharField(max_length=30)
	date_created = models.DateTimeField(default=timezone.now)
	date_posted = models.DateTimeField(blank=True, null=True)

	class Meta:
		ordering = ('date_posted',)
			

	def __str__(self):
		return self.name

	def posted(self):
		self.date_posted=timezone.now()
		self.save()

	def count_comments(self):
		return self.commentss.filter(approved=True)



class Comment(models.Model):
	post = models.ForeignKey('blog.Post',on_delete=models.CASCADE, related_name='commentss')
	author = models.CharField(max_length=50)
	text = models.TextField(blank=True)
	date_created = models.DateTimeField(default=timezone.now)
	approved = models.BooleanField(default=False)

	def __str__(self):
		return self.author

	def approved_comment(self):
		self.approved=True
		self.save()



	