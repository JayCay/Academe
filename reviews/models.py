from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Import profs
from profs.models import Prof
from courses.models import Course

# Create your models here.	
class Review(models.Model):
	message = models.TextField(max_length = 4000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(null = True)
	rating = models.IntegerField(
		default = 5, 
		validators = [MaxValueValidator(5), MinValueValidator(0)]
	)
	prof = models.ForeignKey(Prof, related_name = 'reviews')
	course = models.ForeignKey(Course, related_name = 'reviews')
	user = models.ForeignKey(User, related_name = 'reviews')
	
	def __str__ (self):
		return self.message