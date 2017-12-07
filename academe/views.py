from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.db.models.functions import Concat
from django.db.models import Value
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
import datetime

from courses import views as course_views
from profs import views as prof_views

from reviews.forms import ReviewForm

from profs.models import Prof
from courses.models import Course
from django.contrib.auth.models import User

def index(request):
	"""Landing page, contains the prof and course search"""
	return render(request, 'templates/index.html')

def show_courses_and_profs(request):
	"""
	Shows all of the courses, and the profs under them.
	Interfaces with the prof and course apps, to get
	the data from them
	"""
	courses = course_views.all_courses(request)
	return render(request, 'templates/browse.html', {'courses': courses})

def search(request):
	""" Search function """
	if(request.method == 'POST'):
		prof_query = request.POST.get('prof', None)
		course_query = request.POST.get('course', None)
		if prof_query:
			message = "You searched profs for: " + prof_query
			try:
				# Query profs
				prof_set = Prof.objects.annotate(search_name=Concat('first_name', Value(' '), 'last_name'))
				profs = prof_set.filter(search_name__icontains=prof_query)

				return render(request, 'profs/index.html', {'profs': profs, 'message': message})
			except Prof.DoesNotExist:
				return HttpResponse('No such prof')
		else:
			message = "You searched courses for: " + course_query
			try:
				courses = Course.objects.filter(name__icontains=course_query)
				return render(request, 'courses/index.html', {'courses': courses, 'message': message})
			except Course.DoesNotExist:
				return HttpResponse('No such course')
	else:
		courses = course_views.all_courses(request)
		return render(request, 'templates/browse.html', {'courses': courses})

@login_required
def review(request, prof_id=None):
	""" Review a prof """
	if(request.method=='POST'):
		# Insert the current user, and the prof with the id
		# Happens when review is made through Review
		post_values = request.POST.copy()
		if prof_id:
			post_values['prof'] = prof_id
		post_values['user'] = request.user.id
		print(post_values)
		form = ReviewForm(post_values)
		if(form.is_valid()):
			form.save()
			prof_id = post_values['prof']
			return redirect(reverse('profs_getProf', args=(prof_id,)))
		else:
			print(form.errors)
			return render(request, 'reviews/review_form.html')
	# If there's an input prof, return review page for that prof
	if prof_id:
		user = User.objects.get(pk=request.user.id)
		prof = prof_views.prof(prof_id)
		course = prof.course_set.all()
		data = {'user': user, 'prof': prof}
		review_form = ReviewForm(initial=data)
		review_form.fields['course'].queryset = course
		curr_prof = True
		return render(request, 'reviews/review_form.html', {'review_form': review_form, 'curr_prof': curr_prof, 'prof': prof})
	review_form = ReviewForm()
	return render(request, 'reviews/review_form.html', {'review_form': review_form})
