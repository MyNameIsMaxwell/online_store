from django import forms

from myauth.models import UserProfile
from myorder.models import Order
from mypayment.models import Payment


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["name", "phone_number", "email", "image"]
        widgets = {
            "name": forms.TextInput(attrs={'class': "form-input"}),
            "phone_number": forms.TextInput(attrs={'id': "phone-mask", 'class': "form-input"}),
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


class DeliveryOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_type', 'city', 'address',]

        widgets = {
            "delivery_type": forms.RadioSelect(attrs={'class': "toggle"}),
            "city": forms.TextInput(attrs={'class': "form-input"}),
            "address": forms.Textarea(attrs={'class': "form-textarea"}),
        }

        labels = {
            "delivery_type": "",
            "city": "Город",
            "email": "Адрес",
        }


class PaymentOrderForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_method']

        widgets = {
            "payment_method": forms.RadioSelect(attrs={'class': "toggle"}),
        }

        labels = {
            "payment_method": "",
        }

