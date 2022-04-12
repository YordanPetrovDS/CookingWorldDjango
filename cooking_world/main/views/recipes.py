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
    
# class EditRecipeView(views.UpdateView):
#     template_name = "main/recipe_edit.html"
#     form_class = EditPetForm


# class DeleteRecipeView(views.DeleteView):
#     template_name = "main/recipe_delete.html"
#     form_class = DeletePetForm

# class DetailsRecipeView(auth_mixin.LoginRequiredMixin, views.DetailView):
#     model = PetPhoto
#     template_name = "main/photo_details.html"
#     context_object_name = "pet_photo"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["is_owner"] = self.object.user == self.request.user
#         return context
