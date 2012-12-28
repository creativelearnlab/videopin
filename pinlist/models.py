from django.db import models

# Create your models here.

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
import urllib2
import os
from PIL import Image

class Pin(models.Model):
    piner = models.ForeignKey(User)
    url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.url


    class Meta:
        ordering = ['-id']

