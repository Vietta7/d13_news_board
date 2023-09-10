from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class ConfirmationForm(forms.Form):
    name = forms.CharField(max_length=128)
    code = forms.IntegerField(min_value=10000, max_value=99999)