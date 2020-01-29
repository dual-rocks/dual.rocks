from django.shortcuts import get_object_or_404
from django.http.response import Http404
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from dual_rocks.authentication.models import User
from dual_rocks.user_profile.models import Profile
from dual_rocks.web.forms import CreateProfileForm


def profile_view_resolver(request, at=None):
    user = get_object_or_404(User, at=at)
    is_my_profile = request.user == user
    try:
        profile = user.profile
        return ProfileView.as_view()(request, profile=profile)
    except Profile.DoesNotExist:
        if is_my_profile:
            return CreateProfileView.as_view()(request)
        raise Http404()


class ProfileView(TemplateView):
    template_name = 'web/profile.html'


class CreateProfileView(UpdateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'web/create_profile.html'

    def get_object(self):
        return Profile(user=self.request.user)
