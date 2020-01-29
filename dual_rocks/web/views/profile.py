from django.views.generic import TemplateView


def profile_view_resolver(request, **kwargs):
    return ProfileView.as_view()(request, **kwargs)


class ProfileView(TemplateView):
    template_name = 'web/profile.html'
