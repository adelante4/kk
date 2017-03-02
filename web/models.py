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


class File(models.Model):
    file = models.FileField(upload_to='res/')
    user = models.ForeignKey('User')

    def file_link(self):
        if self.file:
            return "<a href='%s'>download</a>" % (self.file.url,)
        else:
            return "No attachment"
