from django.shortcuts import render, redirect
from django.urls import reverse
from profs.models import Prof
from profs.forms import ProfForm

from reviews.models import Review
from reviews.forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
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
		form = ReviewForm(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect(reverse('profs_index'))

	profs = Prof.objects.all()
	return render(request, 'profs/index.html', {'review_form': ReviewForm, 'profs': profs})

# Display the page of a prof using id passed through url
@login_required
def getProf(request, prof_id):
	prof = Prof.objects.get(pk=prof_id)
	reviews = Review.objects.filter(prof=prof)
	return render(request, 'profs/prof.html', {'review_form': ReviewForm, 'prof': prof, 'reviews': reviews})
	# return redirect(reverse('homepage'))
