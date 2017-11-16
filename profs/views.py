from django.shortcuts import render, redirect
from django.urls import reverse
from profs.models import Prof, Course
from profs.forms import ProfForm
from django.contrib import messages 
from django.contrib.auth.models import User

from reviews.models import Review
from reviews.forms import ReviewForm
from django.contrib.auth.decorators import login_required

def index(request):
	# Make a prof
	# if(request.method=='POST'):
	# 	form = ProfForm(request.POST)
	# 	if(form.is_valid()):
	# 		form.save()
	# 		# Return to profs_index using reverse so only need to change url in settings.py
	# 		return redirect(reverse('profs_index'))

	# Make a new review
	if(request.method=='POST'):
		post_values = request.POST.copy()
		post_values['user'] = request.user.id
		form = ReviewForm(post_values)
		if(form.is_valid()):
			form.save()

			# Go to that profs page
			prof_id = post_values['prof']
			return redirect(reverse('profs_getProf', args=(prof_id)))

	profs = Prof.objects.all()
	return render(request, 'profs/index.html', {'review_form': ReviewForm, 'profs': profs})

# Display the page of a prof using id passed through url
@login_required
def getProf(request, prof_id):
	# Make a new review for the specific prof
	if(request.method=='POST'):
		# Insert the current user, and the prof with the id
		post_values = request.POST.copy()
		post_values['prof'] = prof_id
		post_values['user'] = request.user.id
		form = ReviewForm(post_values)
		if(form.is_valid()):
			form.save()
			return redirect(reverse('profs_getProf', args=(prof_id)))
		else:
			messages.error(request, "Error")
			return render(request, 'profs/prof.html')
	prof = Prof.objects.get(pk=prof_id)
	# prof_course = Course.objects.filter(prof__id = prof_id)
	reviews = Review.objects.filter(prof = prof)
	return render(request, 'profs/prof.html', {'review_form': ReviewForm, 'prof': prof, 'reviews': reviews})
	# return redirect(reverse('homepage'))
