from django.forms import ModelForm, CharField, TextInput
from reviews.models import Review
from profs.models import Prof
from courses.models import Course

from django.forms import widgets
from django.utils.safestring import mark_safe

class ReviewForm(ModelForm):
	rating = CharField(widget=TextInput(attrs={'type': 'number','value': 5, 'min': 0, 'max': 5}))

	class Meta:
		model = Review
		fields = ['message', 'rating', 'prof', 'course', 'user']

	def __init__(self, *args, **kwargs):
		super(ReviewForm, self).__init__(*args, **kwargs)
		self.fields['prof'].widget.attrs['id'] = 'prof'

