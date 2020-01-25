from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LoginView as DjangoLoginView,
    LogoutView as DjangoLogoutView,
)


class HomeView(TemplateView):
    template_name = 'web/home.html'


class LoginView(DjangoLoginView):
    template_name = 'web/login.html'
    next = 'web:home'


class LogoutView(DjangoLogoutView):
    pass
