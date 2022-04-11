from cooking_world.common.helpers import Cuisine, Dificulty, MealType
from cooking_world.common.validators import (
    MaxFileSizeInMbValidator,
    validate_only_letters,
)
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

UserModel = get_user_model()


class Contact(models.Model):
    TITLE_MAX_LENGTH = 100
    TITLE_MIN_LENGTH = 5
    DESCRIPTION_MAX_LENGTH = 400
    DESCRIPTION_MIN_LENGTH = 5

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=[
            MinLengthValidator(TITLE_MIN_LENGTH),
            validate_only_letters,
        ],
    )

    email = models.EmailField()

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=[
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
        ],
    )


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 100
    TITLE_MIN_LENGTH = 5
    IMAGE_UPLOAD_TO_DIR = "recipe/"
    IMAGE_MAX_SIZE_IN_MB = 5
    COOKING_TIME_MIN_VALUE = 1
    SERVINGS_MIN_VALUE = 1
    DESCRIPTION_MAX_LENGTH = 3000
    DESCRIPTION_MIN_LENGTH = 5

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=[
            MinLengthValidator(TITLE_MIN_LENGTH),
            validate_only_letters,
        ],
    )

    photo = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        validators=[
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ],
    )

    cuisine = models.CharField(
        max_length=max(len(x) for x, _ in Cuisine.choices()),
        choices=Cuisine.choices(),
    )

    meal_type = models.CharField(
        max_length=max(len(x) for x, _ in MealType.choices()),
        choices=MealType.choices(),
    )

    dificulty = models.CharField(
        max_length=max(len(x) for x, _ in Dificulty.choices()),
        choices=Dificulty.choices(),
    )

    preparation_time = models.IntegerField(
        validators=[
            MinValueValidator(COOKING_TIME_MIN_VALUE),
        ],
    )

    cooking_time = models.IntegerField(
        validators=[
            MinValueValidator(COOKING_TIME_MIN_VALUE),
        ],
    )

    servings = models.IntegerField(
        validators=[
            MinValueValidator(SERVINGS_MIN_VALUE),
        ],
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=[
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
        ],
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def total_coooking_time(self):
        return self.preparation_time + self.cooking_time


class Blog(models.Model):
    TITLE_MAX_LENGTH = 100
    TITLE_MIN_LENGTH = 5
    DESCRIPTION_MAX_LENGTH = 5000
    DESCRIPTION_MIN_LENGTH = 5
    IMAGE_UPLOAD_TO_DIR = "blog/"
    IMAGE_MAX_SIZE_IN_MB = 5

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=[
            MinLengthValidator(TITLE_MIN_LENGTH),
            validate_only_letters,
        ],
    )

    photo = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        validators=[
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ],
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=[
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
        ],
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
