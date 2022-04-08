from cooking_world.accounts.forms import (
    CreateProfileForm,
    DeleteProfileForm,
    EditProfileForm,
)
from cooking_world.accounts.models import Profile
from cooking_world.common.view_mixins import RedirectToDashboard
from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = "accounts/profile_create.html"
    success_url = reverse_lazy("index")


class UserLoginView(auth_views.LoginView):
    template_name = "accounts/login_page.html"
    success_url = reverse_lazy("index")

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy("index")


class UserEditView:
    pass


class UserDeleteView(views.DeleteView):
    template_name = "accounts/profile_delete.html"
    form_class = DeleteProfileForm


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = "accounts/change_password.html"


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = "accounts/profile_details.html"
    object_context_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a Profile
        # pets = list(Pet.objects.filter(user_id=self.object.user_id))
        # pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()

        # total_likes_count = sum(pp.likes for pp in pet_photos)
        # total_pet_photos_count = len(pet_photos)

        context.update(
            {
                # "total_likes_count": total_likes_count,
                # "total_images_count": total_pet_photos_count,
                "is_owner": self.object.user_id == self.request.user.id,
                # "pets": pets,
            }
        )

        return context
