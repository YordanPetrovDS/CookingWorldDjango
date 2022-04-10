from django.urls import path

from cooking_world.main.views.generic import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
]
