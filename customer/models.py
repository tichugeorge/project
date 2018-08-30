# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	usr_data  = models.OneToOneField(User)
	address = models.CharField(max_length=100)
	place = models.CharField(max_length=100)
	phonenumber=models.CharField(max_length=12)
	zipcode= models.IntegerField()
	profilepic=models.ImageField(upload_to='media/sample_img/')
	

	def __str__(self):
		return self.place