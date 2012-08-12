from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    domain = models.CharField(max_length=250)
    subdomain = models.CharField(max_length=250)

    def __str__(self):  
        return "%s's profile" % self.user 

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

class Weblog(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User)

class Entry(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    pub_date = models.DateTimeField(default=datetime.now())
    summary = models.TextField(null=True, blank=True)
    body = models.TextField()

    weblog = models.ForeignKey(Weblog)
    
    def __unicode__(self):
        return self.title
