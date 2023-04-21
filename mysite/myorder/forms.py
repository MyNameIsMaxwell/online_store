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

