from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	date_written = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	lt = models.FloatField()
	lg = models.FloatField()
	content = models.TextField()

	class Meta:
		ordering = ['-date_written']

	def get_absolute_url(self):
		return reverse('home')