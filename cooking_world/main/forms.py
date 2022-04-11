from cooking_world.common.helpers import BootstrapFormMixin
from cooking_world.common.validators import MaxDateValidator, validate_username
from django import forms

from cooking_world.main.models import Contact


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

