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
    CreatePhotoView,
    set_current_profile,
    unset_current_profile,
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
    path(
        'unset-current-profile/',
        unset_current_profile,
        name='unset_current_profile'
    ),
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
        path(
            'add-photo/',
            required_profile_owner(CreatePhotoView.as_view()),
            name='add_photo'
        ),
        path(
            'set-as-current-profile',
            set_current_profile,
            name='set_as_current_profile'
        )
    ], 'web'), namespace='profile'))
]
