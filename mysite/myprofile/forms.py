from django import forms

from myauth.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["name", "phone_number", "email", "image"]
        widgets = {
            "name": forms.TextInput(attrs={'initial': model.name}),
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
                                   widget=forms.PasswordInput(attrs={'placeholder': 'Тут можно изменить пароль'})
                                   )

        password1 = forms.CharField(max_length=30,
                                   min_length=7,
                                   label="Пароль",
                                   widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль повторно'})
                                   )

    # name = forms.CharField(max_length=50,
    #                        min_length=2,
    #                        label="",
    #                        widget=forms.TextInput(attrs={'placeholder': 'Имя'})
    #                        )
    #
    # phone_number = forms.CharField(max_length=20,
    #                        min_length=2,
    #                        label="",
    #                        widget=forms.TextInput(attrs={'placeholder': 'Имя'})
    #                        )
    #
    # email = forms.EmailField(label="",
    #                          widget=forms.TextInput(attrs={'placeholder': 'E-mail'})
    #                          )
    # password = forms.CharField(max_length=30,
    #                            min_length=7,
    #                            label="",
    #                            widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
    #                            )

