from django.urls import path
from .views import (
    HomeView,
    LoginView,
    LogoutView,
    RegisterView,
    profile_view_resolver,
)

app_name = 'web'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<str:at>/', profile_view_resolver, name='profile')
]
