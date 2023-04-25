from django import forms

from myauth.models import UserProfile


class SortForm(forms.Form):
    name = forms.CharField(max_length=50,
                           min_length=1,
                           label="",
                           required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Название', 'class': "form-input form-input_full"})
                           )

    available = forms.BooleanField(required=False)


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('name', 'phone_number', 'email')
#
#         labels = {
#             'name': "ФИО",
#             'phone_number': "Телефон",
#             'email': "E-mail"
#         }
#
#         widgets = {
#             "name": forms.TextInput(attrs={'class': "form-input"}),
#             "phone_number": forms.TextInput(attrs={'class': "form-input"}),
#             "email": forms.TextInput(attrs={'class': "form-input"}),
#         }
