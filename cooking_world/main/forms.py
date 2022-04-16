import os
from os.path import join

from cooking_world.common.helpers import BootstrapFormMixin
from cooking_world.main.models import Blog, Contact, Recipe
from django import forms
from django.conf import settings
from django.core.validators import MinLengthValidator


class ContactForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    title = forms.CharField(
        max_length=Contact.TITLE_MAX_LENGTH,
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


class EditRecipeForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    # def save(self, commit=True):
    #     db_recipe = Recipe.objects.get(pk=self.instance.id)
    #     if commit:
    #         photo_path = join(settings.MEDIA_ROOT, str(db_recipe.photo))
    #         os.remove(photo_path)
    #     return super().save(commit)

    class Meta:
        model = Recipe
        exclude = ("user",)
        widgets = {
            "type": forms.TextInput(
                attrs={
                    "readonly": "readonly",
                }
            )
        }


class CreateBlogForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        blog = super().save(commit=False)

        blog.user = self.user
        if commit:
            blog.save()

        return blog

    title = forms.CharField(
        validators=[
            MinLengthValidator(Blog.TITLE_MIN_LENGTH),
        ],
    )

    class Meta:
        model = Blog
        exclude = ("user", "publication_date")


class EditBlogForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    # def save(self, commit=True):
    #     db_blog = Blog.objects.get(pk=self.instance.id)
    #     if commit:
    #         photo_path = join(settings.MEDIA_ROOT, str(db_blog.photo))
    #         os.remove(photo_path)
    #     return super().save(commit)

    class Meta:
        model = Blog
        exclude = ("user", "publication_date")
        widgets = {
            "type": forms.TextInput(
                attrs={
                    "readonly": "readonly",
                }
            )
        }
