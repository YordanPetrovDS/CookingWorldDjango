from cooking_world.accounts.models import Gender, Profile
from datetime import date

# from cooking_world.main.forms import CURRENT_DATE
from cooking_world.common.helpers import BootstrapFormMixin
from cooking_world.common.validators import MaxDateValidator, validate_username
from django import forms

# from cooking_world.main.models import PetPhoto
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            username=self.cleaned_data["username"],
            gender=self.cleaned_data["gender"],
            email=self.cleaned_data["email"],
            picture=self.cleaned_data["picture"],
            date_of_birth=self.cleaned_data["date_of_birth"],
            description=self.cleaned_data["description"],
            user=user,
        )

        if commit:
            profile.save()
        return user

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

    gender = forms.ChoiceField(
        choices=Gender.choices(),
    )

    email = forms.EmailField()

    picture = forms.URLField()

    date_of_birth = forms.DateField()

    description = forms.CharField(
        widget=forms.Textarea,
    )

    def clean_date_of_birth(self):
        MaxDateValidator(CreateProfileForm.MAX_DATE_OF_BIRTH)(self.cleaned_data["date_of_birth"])
        return self.cleaned_data["date_of_birth"]

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "picture",
            "description",
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
            "picture": forms.TextInput(
                attrs={
                    "placeholder": "Enter URL",
                }
            ),
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial["gender"] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = "__all__"

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
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Enter username",
                }
            ),
            "picture": forms.TextInput(
                attrs={
                    "placeholder": "Enter URL",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter email",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter description",
                    "rows": 3,
                }
            ),
            "date_of_birth": forms.DateInput(
                attrs={
                    "min": CreateProfileForm.MIN_DATE_OF_BIRTH,
                    "max": CreateProfileForm.MAX_DATE_OF_BIRTH,
                    "type": "date",
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        # Not good
        # should be done with signals
        # because this breaks the abstraction of the auth app
        # pets = list(self.instance.pet_set.all())
        # PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


