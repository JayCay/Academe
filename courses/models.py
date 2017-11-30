from django.db import models

from profs.models import Prof

class Course(models.Model):
	name = models.CharField(max_length = 20, unique = True)
	prof = models.ManyToManyField(Prof)

	def __str__ (self):
		return self.name