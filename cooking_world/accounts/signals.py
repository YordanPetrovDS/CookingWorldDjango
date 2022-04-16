from cooking_world.accounts.models import AppUser, Profile
from django.db.models import signals
from django.dispatch import receiver


@receiver(signals.post_delete, sender=Profile)
def delete_user(instance, **kwargs):
    instance.user.delete()


@receiver(signals.post_save, sender=AppUser)
def save_user(instance, **kwargs):
    if instance.is_superuser:
        profile = Profile(
            first_name="None",
            last_name="None",
            username="None",
            email=instance.email,
            user=instance,
        )
        profile.save()
