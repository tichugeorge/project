# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class NewProducts(models.Model):
	Name=models.CharField(max_length=20)
	quantity=models.CharField(max_length=10)
	price= models.IntegerField()
	picture=models.ImageField(upload_to='sample_img/',null=True,blank=True)
	created_date=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.Name

class BookingProduct(models.Model):
	booked_by=models.ForeignKey(User)
	pdt_types=models.CharField(max_length=100)
	quantity=models.CharField(max_length=100)
	price=models.IntegerField()
	def __str__(self):
		return self.pdt_types

	








