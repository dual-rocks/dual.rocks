import json
from django import forms
from dual_rocks.user_profile.models import Profile


picture_widget = forms.FileInput(
    attrs={
        'data-crop-image-file-input': json.dumps({
            'target': '[name=picture_crop_data]',
            'options': {
                'viewMode': 1,
                'aspectRatio': 1
            }
        })
    }
)


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [
            'user'
        ]
        widgets = {
            'picture': picture_widget
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [
            'user',
            'at',
            'picture',
            'picture_crop_data'
        ]
