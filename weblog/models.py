from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

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
