from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Review
from profs.models import Prof
from .forms import ReviewForm
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def index(request):
	if(request.method=='POST'):
		form = ReviewForm(request.POST)
		form['user'] = User.objects.get(pk=request.user.id)
		if(form.is_valid()):
			form.save()
			# Return to reviews index so that no more post on refresh
			return redirect(reverse('homepage'))
			
	reviews = Review.objects.all()
	profs = Prof.objects.all()
	upload_form = ReviewForm()
	return render(request, 'reviews/index.html', {'reviews': reviews, 'upload_form': upload_form, 'profs': profs})

