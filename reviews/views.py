from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Review
from profs.models import Prof
from .forms import ReviewForm

@login_required()
def index(request):
	if(request.method=='POST'):
		form = ReviewForm(request.POST)
		if(form.is_valid()):
			form.save()
			# Return to reviews index so that no more post on refresh
			return redirect(reverse('homepage'))
			
	reviews = Review.objects.all()
	profs = Prof.objects.all()
	upload_form = ReviewForm()
	return render(request, 'reviews/index.html', {'reviews': reviews, 'upload_form': upload_form, 'profs': profs})

