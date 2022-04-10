from django.shortcuts import redirect
from cooking_world.accounts.forms import (
    CreateProfileForm,
    DeleteProfileForm,
    EditProfileForm,
    LoginUserForm,
    LoginUserForm,
)
from cooking_world.accounts.models import AppUser, Profile
from cooking_world.common.view_mixins import RedirectToDashboard
from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login, logout

# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = "accounts/password_reset.html"
#     email_template_name = "accounts/password_reset_email.html"
#     subject_template_name = "accounts/password_reset_subject"
#     success_message = (
#         "We've emailed you instructions for setting your password, "
#         "if an account exists with the email you entered. You should receive them shortly."
#         " If you don't receive an email, "
#         "please make sure you've entered the address you registered with, and check your spam folder."
#     )
#     success_url = reverse_lazy("index")


class RegisterUserView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = "accounts/profile_create.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    form_class = LoginUserForm
    template_name = "accounts/login_page.html"
    success_url = reverse_lazy("index")

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def form_valid(self, form):
        remember_me = form.cleaned_data.get("remember_me")

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(LoginUserView, self).form_valid(form)


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy("index")


class ChangePasswordUserView(auth_views.PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy("index")


class DetailsProfileView(views.DetailView):
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


class EditProfileView(views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = "accounts/profile_edit.html"

    def get_success_url(self):
        return reverse_lazy(
            "profile details", kwargs={"pk": self.request.user.id}
        )


class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = "accounts/profile_delete.html"
    form_class = DeleteProfileForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)
        user = AppUser.objects.get(id=self.request.user.id)
        user.delete()
        return result
