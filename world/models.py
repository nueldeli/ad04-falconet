from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Coordinate(models.Model):
	lat = models.FloatField()
	lon = models.FloatField()

class Post(models.Model):
	date_written = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	coordinate = models.ForeignKey(Coordinate, on_delete=models.CASCADE)
	content = models.TextField()