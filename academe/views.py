from django.shortcuts import render, redirect
from django.urls import reverse
from profs.models import Prof
from profs.forms import ProfForm

# Homepage
def index(request):
	# if(request.method=='POST'):
	# 	form = ProfForm(request.POST)
	# 	if(form.is_valid()):
	# 		form.save()
	# 		# Return to profs_index using reverse so only need to change url in settings.py
	# 		return redirect(reverse('profs_index'))

	# profs = Prof.objects.all()
	# return render(request, 'profs/index.html', {'prof_form':ProfForm, 'profs': profs})
	return render(request, 'templates/index.html')