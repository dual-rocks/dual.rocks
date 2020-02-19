from django.shortcuts import (
    get_object_or_404,
    redirect,
)
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden
from dual_rocks.user_profile.models import (
    Profile,
    Photo,
)
from dual_rocks.web.forms import (
    CreateProfileForm,
    UpdateProfileForm,
    UpdateProfilePictureForm,
    CreatePhotoForm,
)


def has_profile(fn):
    def wrapper(request, at=None):
        profile = get_object_or_404(Profile, at=at)
        return fn(request, profile=profile)
    return wrapper


def required_profile_owner(fn):
    @has_profile
    def wrapper(request, profile):
        if profile.user != request.user:
            return HttpResponseForbidden()
        return fn(request, profile=profile)
    return wrapper


@has_profile
def profile_view_resolver(request, profile=None):
    if profile.user == request.user:
        return MyProfileView.as_view()(request, profile=profile)
    return ProfileView.as_view()(request, profile=profile)


class ProfileView(TemplateView):
    template_name = 'web/profile.html'


@method_decorator(login_required, name='dispatch')
class MyProfileView(TemplateView):
    template_name = 'web/my_profile.html'


@method_decorator(login_required, name='dispatch')
class CreateProfileView(UpdateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'web/create_profile.html'

    def get_object(self):
        return Profile(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'web/edit_profile.html'

    def get_object(self):
        return self.kwargs.get('profile')


@method_decorator(login_required, name='dispatch')
class UpdateProfilePictureView(UpdateView):
    model = Profile
    form_class = UpdateProfilePictureForm
    template_name = 'web/update_picture.html'

    def get_object(self):
        return self.kwargs.get('profile')


@required_profile_owner
def remove_profile_picture(request, profile):
    profile.picture = None
    profile.save()
    return redirect('web:profile:view', at=profile.at)


@method_decorator(login_required, name='dispatch')
class ProfilesView(TemplateView):
    template_name = 'web/profiles.html'


@method_decorator(login_required, name='dispatch')
class CreatePhotoView(UpdateView):
    model = Photo
    form_class = CreatePhotoForm
    template_name = 'web/add_photo.html'

    def get_object(self):
        return Photo(profile=self.kwargs.get('profile'))
