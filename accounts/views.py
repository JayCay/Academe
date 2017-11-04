from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from accounts.forms import SignUpForm
from accounts.tokens import account_activation_token

# Import the following for sending emails
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

@login_required
def home(request):
	return render(request, 'homepage')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			# subject = 'Activate your Academe Account'
			mess = render_to_string('templates/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,	
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})

			#set up smtp
			s = smtplib.SMTP(host='smtp.gmail.com', port=587)
			s.starttls()
			MY_ADDRESS = "academe.obf@gmail.com"
			s.login(MY_ADDRESS, "Thisisthetester")

			with open("templates/account_activation_email.txt", encoding="utf-8") as template_file:
				template_file_content = template_file.read()
			template_file = Template(template_file_content)

			msg = MIMEMultipart()  # create a message
			message = template_file.substitute(content = str(mess))
			# Setup parameters
			msg['From'] = MY_ADDRESS
			msg['To'] = user.email
			print(user.email)
			msg['Subject'] = "Academe Account Activation"

			msg.attach(MIMEText(message, 'plain'))

			s.send_message(msg)

			del msg

			s.quit()

			# user.email_user(subject, mess)


			return redirect('account_activation_sent')
	else:
		form = SignUpForm()
	return render(request, 'templates/signup.html', {'form' : form})
	
def account_activation_sent(request):
	return render(request, 'templates/account_activation_sent.html')
	
def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, OverflowError, User.DoesNotExist):
		user = None
		
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.profile.email_confirmed= True
		user.save()
		auth_login(request, user)
		return redirect('homepage')
	else:
		return render(request, 'templates/account_activation_invalid.html')
