from cooking_world.common.helpers import BootstrapFormMixin
from cooking_world.common.validators import validate_only_letters
from cooking_world.main.models import Contact, Recipe
from django import forms
from django.core.validators import MinLengthValidator


class ContactForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    title = forms.CharField(
        max_length=Contact.TITLE_MAX_LENGTH,
    )

    description = forms.CharField(
        max_length=Contact.DESCRIPTION_MAX_LENGTH,
    )

    class Meta:
        model = Contact
        fields = "__all__"


class CreateRecipeForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        recipe = super().save(commit=False)

        recipe.user = self.user
        if commit:
            recipe.save()

        return recipe

    title = forms.CharField(
        validators=[
            MinLengthValidator(Recipe.TITLE_MIN_LENGTH),
            validate_only_letters,
        ],
    )

    preparation_time = forms.IntegerField(
        min_value=1,
    )

    cooking_time = forms.IntegerField(
        min_value=1,
    )

    servings = forms.IntegerField(
        min_value=1,
    )

    class Meta:
        model = Recipe
        exclude = ("user",)
