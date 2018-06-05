# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser as AuthUser
# Create your models here.
#class User(AuthUser): # pylint: disable=no-init
#	api_key = models.CharField(max_length=10, default='')

class Article(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	article_name = models.CharField(max_length=255,default='Article name')
	article_post = models.TextField(blank=True, null=True)
	date = models.DateTimeField(null=True, blank=True)


