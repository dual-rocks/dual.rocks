import json
from django import forms
from dual_rocks.user_profile.models import Profile
from dual_rocks.forms import crop_image_from_data


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

    picture_crop_data = forms.CharField()

    def clean_picture(self):
        return crop_image_from_data(self, 'picture', 'picture_crop_data')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [
            'user',
            'at',
            'picture'
        ]
