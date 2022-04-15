from cooking_world.accounts.models import Profile
from cooking_world.main.forms import (
    CreateBlogForm,
    CreateRecipeForm,
    EditBlogForm,
    EditRecipeForm,
)
from cooking_world.main.models import Blog, Recipe
from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views


class CreateBlogView(auth_mixin.LoginRequiredMixin, views.CreateView):
    form_class = CreateBlogForm
    template_name = "main/blog_create.html"
    success_url = reverse_lazy("index")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class DashboardBlogView(views.ListView):
    model = Blog
    template_name = "main/blog_dashboard.html"
    context_object_name = "blogs"
    paginate_by = 6


class EditBlogView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Blog
    form_class = EditBlogForm
    template_name = "main/blog_edit.html"

    def get_success_url(self):
        return reverse_lazy("blog details", kwargs={"pk": self.object.pk})


class DeleteBlogView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Blog
    template_name = "main/blog_delete.html"
    success_url = reverse_lazy("dashboard blogs")
    fields = ()


class DetailsBlogView(views.DetailView):
    model = Blog
    template_name = "main/blog_details.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Profile.objects.get(pk=self.object.user_id)
        context["author"] = author
        context["is_owner"] = self.object.user == self.request.user
        return context
