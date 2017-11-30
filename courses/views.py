from django.shortcuts import render, redirect
from django.urls import reverse
from profs.models import Prof
from profs.forms import ProfForm
from .models import Course
from django.contrib import messages 
from django.contrib.auth.models import User

from reviews.models import Review
from reviews.forms import ReviewForm
from django.contrib.auth.decorators import login_required

def index(request):
	"""Show all the courses"""
	courses = Course.objects.all()
	return render(request, 'courses/index.html', {'courses': courses})
