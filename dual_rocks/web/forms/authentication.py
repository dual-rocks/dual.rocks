from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from dual_rocks.authentication.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return make_password(password)
