from datetime import date

from cooking_world.accounts.models import AppUser, Gender, Profile
from cooking_world.common.helpers import BootstrapFormMixin
from cooking_world.common.validators import MaxDateValidator, validate_username
from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model, login, logout
from django.core.validators import MinLengthValidator

MIN_DATE_OF_BIRTH = str(date(1920, 1, 1))
MAX_DATE_OF_BIRTH = str(date.today())


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    username = forms.CharField(
        validators=[
            MinLengthValidator(Profile.USERNAME_MIN_LEN),
            validate_username,
        ],
    )

    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )

    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            user=user,
        )
        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
        )
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter first name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter last name",
                }
            ),
            "password1": forms.PasswordInput(
                attrs={
                    "placeholder": "Password",
                    "data-toggle": "password",
                    "id": "password",
                }
            ),
            "password2": forms.PasswordInput(
                attrs={
                    "placeholder": "Confirm Password",
                    "data-toggle": "password",
                    "id": "password",
                }
            ),
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial["gender"] = Gender.DO_NOT_SHOW

    class Meta:
        model = Profile
        exclude = (
            "email",
            "user",
        )

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "label": "First Name",
                    "placeholder": "Enter first name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "label": "Last Name",
                    "placeholder": "Enter last name",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "label": "Username",
                    "placeholder": "Enter username",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "label": "Email",
                    "placeholder": "Enter email",
                }
            ),
            "picture": forms.TextInput(
                attrs={
                    "label": "Avatar",
                    "placeholder": "Enter URL",
                }
            ),
            "date_of_birth": forms.DateInput(
                attrs={
                    "label": "Date of Birth",
                    "min": MIN_DATE_OF_BIRTH,
                    "max": MAX_DATE_OF_BIRTH,
                    "type": "date",
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class LoginUserForm(auth_forms.AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
            }
        ),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                "data-toggle": "password",
                "id": "password",
                "name": "password",
            }
        ),
    )

    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = AppUser
        fields = [
            "username",
            "password",
            "remember_me",
        ]
