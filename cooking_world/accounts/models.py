import datetime
from enum import Enum

from cooking_world.accounts.managers import AppUserManager
from cooking_world.common.validators import (
    validate_only_letters,
    validate_username,
)
from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Gender(ChoicesMixin, Enum):
    MALE = "Male"
    FEMALE = "Female"
    DO_NOT_SHOW = "Do not show"


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = "email"

    objects = AppUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 25
    USERNAME_MAX_LEN = 20
    USERNAME_MIN_LEN = 7

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=[
            MinLengthValidator(USERNAME_MIN_LEN),
            validate_username,
        ],
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        ],
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        ],
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in Gender.choices()),
        choices=Gender.choices(),
        null=True,
        blank=True,
        default=Gender.DO_NOT_SHOW,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    picture = models.URLField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year
