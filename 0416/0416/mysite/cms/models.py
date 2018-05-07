from django.db import models


class Intro(models.Model):
	name=models.CharField(max_length=8)
	hobby=models.CharField(max_length=8)
	food=models.CharField(max_length=8)
	def __str__(self):
		return self.name