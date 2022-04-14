from cooking_world.main.views.generic import ContactView, HomeView
from cooking_world.main.views.recipes import (
    CreateRecipeView,
    DashboardRecipeView,
    DeleteRecipeView,
    DetailsRecipeView,
)
from django.urls import path

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("create-recipe/", CreateRecipeView.as_view(), name="create recipe"),
    path(
        "dashboard-recipes/",
        DashboardRecipeView.as_view(),
        name="dashboard recipes",
    ),
    path(
        "recipes/<int:pk>/", DetailsRecipeView.as_view(), name="recipe details"
    ),
    path(
        "recipes/<int:pk>/delete/", DeleteRecipeView.as_view(), name="delete recipe"
    ),
]
