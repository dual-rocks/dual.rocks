from django.urls import path
from .views import (
    HomeView,
    LoginView,
    LogoutView,
    RegisterView,
    ProfileView,
)

app_name = 'web'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<slug:at>/', ProfileView.as_view(), name='profile')
]
