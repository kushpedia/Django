from django.db.models.signals import post_save, post_delete
from . models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

# @receiver(post_save, sender=Profile)
# create a profile everytime a User is created
def createProfile(sender, instance,created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            user_name = user.username,
            email = user.email,
            name = user.first_name,
        )
        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )
        
        
# delete user when a profile is deleted
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()   

# update user on saving the profile
def updateUser(sender, instance, created,**kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name,
        user.username = profile.user_name,
        user.email = profile.email,
    
    

post_save.connect(createProfile,sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)