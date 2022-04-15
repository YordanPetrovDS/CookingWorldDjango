from cooking_world.accounts.views import (
    ChangePasswordUserView,
    DeleteProfileView,
    DetailsProfileView,
    EditProfileView,
    LoginUserView,
    LogoutUserView,
    RegisterUserView,
)
from django.urls import path

urlpatterns = (
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("<int:pk>/", DetailsProfileView.as_view(), name="profile details"),
    path(
        "profile/<int:pk>/edit/",
        EditProfileView.as_view(),
        name="edit profile",
    ),
    path(
        "profile/<int:pk>/delete/",
        DeleteProfileView.as_view(),
        name="delete profile",
    ),
    path(
        "password-change/",
        ChangePasswordUserView.as_view(),
        name="password change",
    ),
)

import cooking_world.accounts.signals