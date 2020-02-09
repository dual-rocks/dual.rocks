from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from dual_rocks.user_profile.models import Profile
from dual_rocks.web.forms import (
    CreateProfileForm,
    UpdateProfileForm,
)


def has_profile(fn):
    def wrapper(request, at=None):
        profile = get_object_or_404(Profile, at=at)
        return fn(request, profile=profile)
    return wrapper


@has_profile
def profile_view_resolver(request, profile=None):
    if profile.user == request.user:
        return MyProfileView.as_view()(request, profile=profile)
    return ProfileView.as_view()(request, profile=profile)


class ProfileView(TemplateView):
    template_name = 'web/profile.html'


class MyProfileView(TemplateView):
    template_name = 'web/my_profile.html'


class CreateProfileView(UpdateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'web/create_profile.html'

    def get_object(self):
        return Profile(user=self.request.user)


class EditProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'web/edit_profile.html'

    def get_object(self):
        return self.kwargs.get('profile')


@method_decorator(login_required, name='dispatch')
class ProfilesView(TemplateView):
    template_name = 'web/profiles.html'
