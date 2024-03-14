from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Check if this is a new user instance being created
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # For existing users, get_or_create the UserProfile
        UserProfile.objects.get_or_create(user=instance)
        # Now you're safe to save the profile, knowing it exists
        instance.profile.save()
