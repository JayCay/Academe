from django.forms import ModelForm
from .models import Prof, Review

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['message', 'rating', 'prof']