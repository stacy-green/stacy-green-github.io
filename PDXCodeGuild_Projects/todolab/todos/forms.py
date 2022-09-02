from django import forms
from .models import Priority


class AuthForm(forms.Form):
    username = forms.CharField(max_length=12, label="Username")
    password = forms.CharField(max_length=12, label="Password", widget=forms.PasswordInput)

class NewTodoForm(forms.Form):
    text = forms.CharField(max_length=240)
    priority = forms.CharField(max_length=10, widget=forms.Select(choices=Priority.objects.all().values_list('id','name')))
