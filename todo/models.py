from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime   


# Create your models here.

class Task(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,  null=True, blank=True, on_delete=models.SET_NULL)
	title=models.CharField(max_length=30)
	description=models.TextField(max_length=100)
	deadline = models.DateTimeField(default=datetime.now(), blank=True)
	complete=models.CharField(max_length=10,default="False")
	status=models.CharField(max_length=10,default="Incomplete")
	#slug=models.SlugField(unique=True)
	#date=timezone.now()