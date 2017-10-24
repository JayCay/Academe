from django.db import models

# Create your models here.
class Prof(models.Model):
	first_name = models.CharField(max_length = 20, unique = False)
	last_name = models.CharField(max_length = 20, unique = False)
	
	def __str__ (self):
		return self.first_name + self.last_name