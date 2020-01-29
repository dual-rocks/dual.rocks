from django.views.generic import TemplateView


class ProfileView(TemplateView):
    def get_template_names(self):
        return 'web/profile.html'
