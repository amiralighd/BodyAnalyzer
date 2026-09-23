from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('phone_number', 'password1', 'password2')


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        phone_number = cleaned_data.get('phone_number')
        password = cleaned_data.get('password')

        if phone_number and password:
            user = authenticate(
                username=phone_number,
                password=password
            )

            if user is None:
                raise forms.ValidationError(
                    'Phone number or password is incorrect.'
                )

            self.user = user

        return cleaned_data

    def get_user(self):
        return self.user