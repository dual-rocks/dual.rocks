from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import (
    LoginView as DjangoLoginView,
    LogoutView as DjangoLogoutView,
)
from django.contrib.auth import login
from dual_rocks.authentication.models import User
from dual_rocks.web.forms import RegisterForm


class HomeView(TemplateView):
    template_name = 'web/home.html'


class LoginView(DjangoLoginView):
    template_name = 'web/login.html'
    next = 'web:home'


class LogoutView(DjangoLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'web/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
