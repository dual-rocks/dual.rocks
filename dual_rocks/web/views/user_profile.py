from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from dual_rocks.user_profile.models import Profile
from dual_rocks.web.forms import CreateProfileForm


def profile_view_resolver(request, at=None):
    profile = get_object_or_404(Profile, at=at)
    return ProfileView.as_view()(request, profile=profile)


class ProfileView(TemplateView):
    template_name = 'web/profile.html'


class CreateProfileView(UpdateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'web/create_profile.html'

    def get_object(self):
        return Profile(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class ProfilesView(TemplateView):
    template_name = 'web/profiles.html'
