from cooking_world.main.views.generic import ContactView, HomeView
from cooking_world.main.views.recipes import CreateRecipeView
from django.urls import path

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("create-recipe/", CreateRecipeView.as_view(), name="create recipe"),
]
