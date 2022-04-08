import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_username(string):
    if not re.match("^[a-zA-Z0-9_]+$", string):
        raise ValidationError(
            "Ensure this value contains only letters, numbers, and underscore."
        )


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Value must contain only letters")


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(f"Max file size is {self.max_size:.2f} MB")

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024


@deconstructible
class MinDateValidator:
    def __init__(self, min_date):
        self.min_date = min_date

    def __call__(self, value):
        if value < self.min_date:
            raise ValidationError(f'Date must be greater than {self.min_date}')


@deconstructible
class MaxDateValidator:
    def __init__(self, max_date):
        self.max_date = max_date

    def __call__(self, value):
        if self.max_date < value:
            raise ValidationError(f'Date must be earlier than {self.max_date}')