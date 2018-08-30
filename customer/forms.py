from django import forms
from customer.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		exclude = ('usr_data',)

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','email','username','password1','password2']