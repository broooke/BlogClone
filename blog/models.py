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