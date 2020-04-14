from django import forms
from django.contrib.auth.models import User
from uspa.models import userprofile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username','email','password')


class userprofileform(forms.ModelForm):
	class Meta():
		model = userprofile
		fields =('portfolio_site','profile_pic')
