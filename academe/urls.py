"""academe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views

from reviews import views as reviews_views

from profs import views as profs_views

urlpatterns = [
	url(r'^signup/$', accounts_views.signup, name='signup'),
	url(r'^account_activation_sent/$', accounts_views.account_activation_sent, name='account_activation_sent'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        accounts_views.activate, name='activate'),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='templates/login.html'), name='login'),
	url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', reviews_views.index, name="reviews_index"),
    url(r'^profs/', profs_views.index, name="profs_index"),
]
