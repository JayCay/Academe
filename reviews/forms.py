from django.forms import ModelForm, CharField, TextInput
from reviews.models import Review

# Make a custom widget for rating so it can only be 0 - 5
from django.forms import widgets
from django.utils.safestring import mark_safe

# class RatingWidget(widgets.TextInput):
	# def render(self, name, value, attrs=None):
		# return mark_safe(u'''<span>USD</span>%s''' % (super(RatingWidget, self).render(name, value, attrs)))

class ReviewForm(ModelForm):
	# rating = CharField(label='Cost Price Per Unit', widget=RatingWidget, max_length=5)
	rating = CharField(widget=TextInput(attrs={'type': 'number','value': 5, 'min': 0, 'max': 5}))
	
	class Meta:
		model = Review
		fields = ['message', 'rating', 'prof', 'user']