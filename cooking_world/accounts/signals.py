from cooking_world.accounts.models import Profile
from django.db.models import signals
from django.dispatch import receiver


@receiver(signals.post_delete, sender=Profile)
def delete_user(instance, **kwargs):
    instance.user.delete()
