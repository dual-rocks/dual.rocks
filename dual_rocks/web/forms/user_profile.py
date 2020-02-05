import json
from django import forms
from dual_rocks.user_profile.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [
            'user'
        ]
        widgets = {
            'picture': forms.FileInput(
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
        }
