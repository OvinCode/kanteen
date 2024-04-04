from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
       model = User
       fields = ['first_name', 'last_name', 'username', 'email', 'password']




