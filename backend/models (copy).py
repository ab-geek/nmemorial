from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Access(models.Model):
    user_email = models.CharField(max_length=100,blank=False)
    password = models.CharField(max_length=100)
    creation_date = models.DateField()
    authorised = models.IntegerField()
    email_verify_code = models.CharField(max_length=255)

    def __unicode__(self):
        return self.user_email

class DocumentGallery(models.Model):
    memorial_guid = models.IntegerField(blank=False)
    documentname = models.CharField(max_length=255)
    documentlocation = models.CharField(max_length=255)

    def __unicode__(self):
        return self.documentname

class PhotoGallery(models.Model):
    memorial_guid = models.IntegerField(blank=False)
    photoname = models.CharField(max_length=255)

    def __unicode__(self):
        return self.photoname

class ResetPassword(models.Model):
    emailid = models.CharField(max_length=255,blank=False)
    code = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.emailid

class VideoGallery(models.Model):
    memorial_guid = models.IntegerField()
    videoname = models.CharField(max_length=255)
    videolocation = models.CharField(max_length=255)

    def __unicode__(self):
        return self.videoname
