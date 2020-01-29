from django import forms
from django.contrib.auth.hashers import make_password
from dual_rocks.authentication.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'at',
            'email',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput
        }

    def clean_password(self):
        return make_password(self.cleaned_data.get('password'))
