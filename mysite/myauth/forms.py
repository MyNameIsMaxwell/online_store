from django.contrib.auth.models import Group
from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=50,
                           min_length=2,
                           label="",
                           widget=forms.TextInput(attrs={'placeholder': 'Имя'})
                           )
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'placeholder': 'E-mail'})
                             )
    password = forms.CharField(max_length=30,
                               min_length=7,
                               label="",
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
                               )


class LoginForm(forms.Form):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'placeholder': 'E-mail'})
                             )
    password = forms.CharField(max_length=30,
                               min_length=7,
                               label="",
                               widget=forms.PasswordInput(attrs={'placeholder': '********'})
                               )
# print(RegisterForm(auto_id=False))

