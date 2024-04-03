from django.db.models.signals import pre_save #signals that are executed at instant before the model instance is saved
from django.contrib.auth.models import User

# setting up the authentication with email instead of username, but better method is to overwrite the User model
def updateUser(sender,  instance, **kwargs):
    user = instance
    if user.email != '':
        user.username = user.email

pre_save.connect(updateUser, sender=User)