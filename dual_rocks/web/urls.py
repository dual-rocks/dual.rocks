from django.urls import path, include
from .views import (
    required_profile_owner,
    HomeView,
    LoginView,
    LogoutView,
    RegisterView,
    CreateProfileView,
    ProfilesView,
    profile_view_resolver,
    EditProfileView,
    UpdateProfilePictureView,
    remove_profile_picture,
)

app_name = 'web'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path(
        'create-profile/',
        CreateProfileView.as_view(),
        name='create-profile'
    ),
    path('profiles/', ProfilesView.as_view(), name='profiles'),
    path('<str:at>/', include(([
        path('', profile_view_resolver, name='view'),
        path(
            'edit/',
            required_profile_owner(EditProfileView.as_view()),
            name='edit'
        ),
        path(
            'update-picture/',
            required_profile_owner(UpdateProfilePictureView.as_view()),
            name='update_picture'
        ),
        path('remove-picture/', remove_profile_picture, name='remove_picture'),
    ], 'web'), namespace='profile'))
]
