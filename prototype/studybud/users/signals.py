# when signals are in different file, they won't run by default, so we need to import them in the main app file, in this case, users/apps.py

from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile


#@receiver(post_save, sender=Profile) # decorator to connect signal to function
def createProfile(sender, instance, created, **kwargs):
    print('SIgnAL tRRigGerrRED!')
    if created:
        user = instance
        profile = Profile.objects.create(user=user, username=user.username, email=user.email, name=user.first_name)
    

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user # one to one relationship
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
   

post_save.connect(createProfile, sender=User) # connect signal to function
post_save.connect(updateUser, sender=Profile) # any time a profile is updated, this function will be triggered
post_delete.connect(deleteUser, sender=Profile) 