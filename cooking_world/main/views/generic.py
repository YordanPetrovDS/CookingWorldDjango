from cooking_world.main.forms import ContactForm
from django.urls import reverse_lazy
from django.views import generic as views

from cooking_world.main.models import Contact


class HomeView(views.TemplateView):
    template_name = "main/home_page.html"


class ContactView(views.CreateView):
    form_class = ContactForm
    template_name = "main/contact_page.html"
    success_url = reverse_lazy("index")
