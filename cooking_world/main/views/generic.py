from cooking_world.main.forms import ContactForm
from cooking_world.main.models import Blog, Recipe
from django.urls import reverse_lazy
from django.views import generic as views


class HomeView(views.ListView):
    model = Recipe
    template_name = "main/home_page.html"
    context_object_name = "recipes"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blog.objects.all()
        context["blogs"] = blogs
        return context


class ContactView(views.CreateView):
    form_class = ContactForm
    template_name = "main/contact_page.html"
    success_url = reverse_lazy("index")
