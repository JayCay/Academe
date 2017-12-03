from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Concat
from django.db.models import Value
from django.contrib import messages 
import json

from profs.models import Prof
from .models import Course
from django.contrib.auth.models import User
from reviews.models import Review

from profs.forms import ProfForm
from reviews.forms import ReviewForm


def index(request):
	"""Show all the courses"""
	courses = all_courses()
	return render(request, 'courses/index.html', {'courses': courses})

def all_courses(request):
	"""Returns all the courses in the database"""
	courses = Course.objects.all()
	return courses

def prof_courses(request, prof_id):
	""" Return the courses of a specific prof"""
	course = Course.objects.filter(prof=prof_id)
	return course

def json_prof_courses(request, prof_name):
	""" Returns the JSON of courses of a specific prof for xhr"""	
	prof_set = Prof.objects.annotate(search_name=Concat('first_name', Value(' '), 'last_name'))
	prof_id = prof_set.filter(search_name__icontains=prof_name)
	courses = prof_courses(request, prof_id)

	# Get all the courses
	all_courses = {}
	for course in courses:
		all_courses[course.pk] = course.name

	# data = serializers.serialize('json', all_courses)
	data = json.dumps(all_courses)
	return HttpResponse(data, content_type="application/json")

