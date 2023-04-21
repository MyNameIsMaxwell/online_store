from django import forms

from myauth.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["name", "phone_number", "email", "image"]
        widgets = {
            "name": forms.TextInput(attrs={'class': "form-input",

                                           }),
            "phone_number": forms.TextInput(attrs={'class': "form-input",}),
            "email": forms.TextInput(attrs={'class': "form-input"}),
            "image": forms.FileInput(attrs={"class": "Profile-fileLabel Profile-file"}),
        }
        labels = {
            "name": "ФИО",
            "phone_number": "Телефон",
            "email": "E-mail",
            "image": "Аватар",
        }

    password = forms.CharField(max_length=30,
                               min_length=7,
                               label="Пароль",
                               required=False,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Тут можно изменить пароль'})
                               )

    password1 = forms.CharField(max_length=30,
                                min_length=7,
                                label="Подтверждение пароля",
                                required=False,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль повторно'})
                                )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password1 = cleaned_data.get('password1')

        if password and password1 and password != password1:
            raise forms.ValidationError("Пароли не совпадают")