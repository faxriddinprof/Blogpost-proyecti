from django import forms
from django.core.exceptions import ValidationError

class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=3, label='UserName', required=True)
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(),
    )


    def clean_username(self):
        username = self.cleaned_data["username"]
        if 'aaaaa' not in username:
            raise ValidationError('Usernami ichida aaa yuq')
    