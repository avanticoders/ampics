from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

from django.contrib.auth.models import User

from .models import Account, Upload

@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Account.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email
        )