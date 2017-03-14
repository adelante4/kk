from django.db import models
import os
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_delete
# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255, default="")
    email = models.EmailField(default="")
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __unicode__(self):
        return "{} {}".format(self.fname,self.lname)


class File(models.Model):
    file = models.FileField(upload_to='res/')
    user = models.ForeignKey('User')


@receiver(post_delete,sender = File)
def fileDelete(sender, instance, **kwargs):
    if(instance.file):
        instance.file.delete(False)