from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(), help_text='Required. Inform a valid email address.')
	
	def clean_email(self):
		data = self.cleaned_data['email']
		if "@obf.ateneo.edu" not in data:   # any check you need
			raise forms.ValidationError("Please use your obf email.")
		return data
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')