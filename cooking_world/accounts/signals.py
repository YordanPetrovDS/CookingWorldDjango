from django.db.models import signals
from django.dispatch import receiver

from cooking_world.accounts.models import AppUser, Profile


@receiver(signals.post_delete, sender=Profile)
def delete_user(instance, **kwargs):
    profile = instance if instance else None
    user = AppUser.objects.get(pk=profile.pk)
    user.delete()
    profile.delete()
    print("User deleted")
