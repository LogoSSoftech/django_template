import os

from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractUser


# -----------------------USERS--------------------------#

class User(AbstractUser):

    '''
    Brief Users
    '''
    profile_picture = models.ImageField(
        upload_to='img/users',
        blank=True,
        null=True,
        verbose_name="Profile Picture",
        default='default/default_avatar.png')
    profile_cover = models.ImageField(
        upload_to='img/users',
        blank=True,
        null=True,
        verbose_name="Profile Cover",
        default='default/default_cover.jpg')

    class Meta:
        verbose_name = 'Users'
        db_table = 'users'

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name()

    @receiver(pre_save, sender='core.User')
    def event_handler(sender, instance, **kwargs):

        '''
        Delete old profile picture
        '''

        try:
            old_picture = ''
            old_instance = sender.objects.get(id=instance.id)

            if old_instance.profile_picture != instance.profile_picture:
                old_picture = old_instance.profile_picture
            elif old_instance.profile_cover != instance.profile_cover:
                old_picture = old_instance.profile_cover

            if old_picture != '' and str(old_picture)[:7] != "default":
                os.remove(str(settings.BASE_DIR) +
                          '/media/' + str(old_picture))
            return True
        except Exception:
            return True
