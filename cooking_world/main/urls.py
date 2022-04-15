from cooking_world.main.views.blogs import (
    CreateBlogView,
    DashboardBlogView,
    DeleteBlogView,
    DetailsBlogView,
    EditBlogView,
)
from cooking_world.main.views.generic import ContactView, HomeView
from cooking_world.main.views.recipes import (
    CreateRecipeView,
    DashboardRecipeView,
    DeleteRecipeView,
    DetailsRecipeView,
    EditRecipeView,
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
        "recipes/<int:pk>/",
        DetailsRecipeView.as_view(),
        name="recipe details",
    ),
    path(
        "recipes/<int:pk>/edit/",
        EditRecipeView.as_view(),
        name="edit recipe",
    ),
    path(
        "recipes/<int:pk>/delete/",
        DeleteRecipeView.as_view(),
        name="delete recipe",
    ),
    path("create-blog/", CreateBlogView.as_view(), name="create blog"),
    path(
        "dashboard-blogs/",
        DashboardBlogView.as_view(),
        name="dashboard blogs",
    ),
    path("blogs/<int:pk>/", DetailsBlogView.as_view(), name="blog details"),
    path("blogs/<int:pk>/edit/", EditBlogView.as_view(), name="edit blog"),
    path(
        "blogs/<int:pk>/delete/",
        DeleteBlogView.as_view(),
        name="delete blog",
    ),
]

import cooking_world.main.signals