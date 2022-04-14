from cooking_world.main.forms import CreateRecipeForm
from cooking_world.main.models import Recipe
from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views


class CreateRecipeView(auth_mixin.LoginRequiredMixin, views.CreateView):
    form_class = CreateRecipeForm
    template_name = "main/recipe_create.html"
    success_url = reverse_lazy("index")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class DashboardRecipeView(views.ListView):
    model = Recipe
    template_name = "main/recipe_dashboard.html"
    context_object_name = "recipes"
    paginate_by = 6


# class EditRecipeView(views.UpdateView):
#     template_name = "main/recipe_edit.html"
#     form_class = EditPetForm


class DeleteRecipeView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Recipe
    template_name = "main/recipe_delete.html"
    success_url = reverse_lazy("dashboard recipes")
    fields = ()


class DetailsRecipeView(views.DetailView):
    model = Recipe
    template_name = "main/recipe_details.html"
    context_object_name = "recipe"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_owner"] = self.object.user == self.request.user
        return context
