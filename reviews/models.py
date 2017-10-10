from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length = 15, unique = True)
	description = models.CharField(max_length = 100)

class Prof(models.Model):
	first_name = models.CharField(max_length = 20, unique = False)
	last_name = models.CharField(max_length = 20, unique = False)
	
	def __str__ (self):
		return self.first_name + self.last_name
	
	
class Review(models.Model):
	message = models.TextField(max_length = 4000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(null = True)
	rating = models.IntegerField(
		default = 5, 
		validators = [MaxValueValidator(5), MinValueValidator(0)]
	)
	prof = models.ForeignKey(Prof, related_name = 'reviews')
	
	def __str__ (self):
		return self.message