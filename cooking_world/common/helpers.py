from enum import Enum

from django.forms import ChoiceField


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(x.value, x.value) for x in cls]


class Gender(ChoicesMixin, Enum):
    MALE = "Male"
    FEMALE = "Female"
    DO_NOT_SHOW = "Do not show"


class MealType(ChoicesMixin, Enum):
    BREAKFAST = "Breakfast"
    STARTER = "Starter"
    LUNCH = "Lunch"
    DINNER = "Dinner"
    DESSERT = "Dessert"


class Dificulty(ChoicesMixin, Enum):
    NOVICE = "Novice"
    ADVANCED = "Advanced"
    EXPERT = "Expert"


class Cuisine(ChoicesMixin, Enum):
    FRENCH = "French"
    ITALIAN = "Italian"
    BULGARIAN = "Bulgarian"
    CHINESE = "Chinese"
    GREEK = "Greek"
    JAPANESE = "Japanese"
    INDIAN = "Indian"
    SPANISH = "Spanish"
    MOROCCAN = "Moroccan"
    LEBANESE = "Lebanese"
    MEDITERRANEAN = "Mediterranean"
    TURKISH = "Turkish"
    THAI = "Thai"


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, "attrs"):
                setattr(field.widget, "attrs", {})
            if "class" not in field.widget.attrs:
                field.widget.attrs["class"] = ""
            field.widget.attrs["class"] += "form-control"


class DisabledFieldsFormMixin:
    disabled_fields = "__all__"
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            if (
                self.disabled_fields != "__all__"
                and name not in self.disabled_fields
            ):
                continue

            if not hasattr(field.widget, "attrs"):
                setattr(field.widget, "attrs", {})

            if isinstance(field, ChoiceField):
                field.widget.attrs["disabled"] = "disabled"
            else:
                field.widget.attrs["readonly"] = "readonly"
