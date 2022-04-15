import os
from os.path import join

from cooking_world.main.models import Blog
from django.conf import settings
from django.db.models import signals
from django.dispatch import receiver


@receiver(signals.pre_delete, sender=Blog)
def delete_blog_photo(instance, **kwargs):
    db_blog = Blog.objects.get(id=instance.id)
    blog_photo = db_blog.photo
    photo_path = join(settings.MEDIA_ROOT, str(blog_photo))
    os.remove(photo_path)
