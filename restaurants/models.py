from django.db import models

#Create your models here.

class restaurants(models.Model):
	name = models.CharField(max_length = 120)		
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()


	def __str__(self):
		return self.name
