from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255, default="")
    email = models.EmailField(default="")
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __unicode__(self):
        return "{} {}".format(self.fname,self.lname)
0