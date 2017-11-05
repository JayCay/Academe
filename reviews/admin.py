from django.contrib import admin

# Register your models here.
from .models import Course, Review
admin.site.register(Course)
admin.site.register(Review)