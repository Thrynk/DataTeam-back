from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages




# class formName(forms.Form)
# f['subject'].label_tag(attrs={'class': 'foo'})

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username=username.lower()
        list =  User.objects.filter(username=username) #renvois une list des users avec cet username
        if not list.count():
            raise ValidationError(
                ('Any acount with the username : %(value)s'),
                code='invalid',
                params={'value': username},
                )
        return username

    def process(self,request):
        user = authenticate(
            request,
            username=self.cleaned_data.get("username"),
            password=self.cleaned_data.get("password")
            )
        return user


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Password1", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Password2", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username=username.lower()
        list =  User.objects.filter(username=username) #renvois une list des users avec cet username
        if list.count():
            raise ValidationError(
                ('Username %(value)s already taken'),
                code='invalid',
                params={'value': username},
                )
        else:
            return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        list=User.objects.filter(email=email)
        if list.count():
            raise ValidationError(
                ('Username %(value)s already taken'),
                code='invalid',
                params={'value': email},
                )
        else:
            return email

        def clean_password2(self):
            password1=self.cleaned_data.get('password1')
            password2=self.cleaned_data.get('password2')
            if password1 != password2:
                 raise ValidationError(
                    ("Passwords don't match"),
                    code='invalid',
                    params={},
                    )
            else:
                return password2

    def process(self):
        user = User.objects.create_user(
            username = self.cleaned_data.get("username"),
            email = self.cleaned_data.get("email"),
            password = self.cleaned_data.get("password2")
        )
        return user
