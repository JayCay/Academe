from django.shortcuts import render
from .models import Review, Prof
from .forms import ReviewForm

# Create your views here.
def index(request):
	if(request.method=='POST'):
		form = ReviewForm(request.POST)
		if(form.is_valid()):
			form.save()
			
	reviews = Review.objects.all()
	profs = Prof.objects.all()
	upload_form = ReviewForm()
	return render(request, 'index.html', {'reviews': reviews, 'upload_form': upload_form, 'profs': profs})

