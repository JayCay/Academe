from django.forms import ModelForm
from profs.models import Prof

class ProfForm(ModelForm):
	class Meta:
		model = Prof
		fields = ['first_name', 'last_name']