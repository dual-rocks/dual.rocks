from django import forms
from dual_rocks.user_profile.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [
            'user'
        ]
