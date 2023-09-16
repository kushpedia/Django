from django.db import models
from django.contrib.auth.models import User
import uuid


# # Sending email notifications on signals detection
# import smtplib

# EMAIL = "kushpedia2023py@gmail.com"
# PASSWORD = "ywxbxtgtvdqxhxxg"
# # smtp connection
# conn = smtplib.SMTP("smtp@gmail.com")
# conn.starttls
# conn.login(user=EMAIL, password=PASSWORD)
# # Create your models here.

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    user_name = models.CharField(max_length=200,null=True, blank=True)
    location = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.FileField(null=True, blank=True, 
                                    upload_to='profiles/', default="profiles/user-default.png")
    social_github = models.CharField(max_length=200,null=True, blank=True)
    social_facebook = models.CharField(max_length=200,null=True, blank=True)
    social_twitter = models.CharField(max_length=200,null=True, blank=True)
    social_linkedin = models.CharField(max_length=200,null=True, blank=True)
    social_youtube = models.CharField(max_length=200,null=True, blank=True)
    social_website = models.CharField(max_length=200,null=True, blank=True)
    created =models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False, 
                            primary_key=True)
    
    def __str__(self):
        return str(self.user.username)
    
class Skill(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created =models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,editable=False, 
                            primary_key=True)
    
    def __str__(self):
        return str(self.name)

