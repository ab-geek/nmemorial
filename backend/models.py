from __future__ import unicode_literals

from django.db import models


class Access(models.Model):
    guid = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    creation_date = models.DateField()
    authorised = models.IntegerField()
    email_varify_code = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'access'

    def __unicode__(self):
        return self.user_email


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DocumentGallery(models.Model):
    guid = models.AutoField(primary_key=True)
    memorial_guid = models.IntegerField()
    documentname = models.CharField(max_length=100)
    documentlocation = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'documentgallery'

    def __unicode__(self):
        return self.documentname


class Memorial(models.Model):
    guid = models.AutoField(primary_key=True)
    accessguid = models.IntegerField()
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    dod = models.DateField(db_column='DOD')  # Field name made lowercase.
    latitude = models.DecimalField(max_digits=10, decimal_places=4)
    longitude = models.DecimalField(max_digits=10, decimal_places=4)
    story = models.TextField()
    relatedlink = models.CharField(max_length=100)
    profilephoto = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memorial'

    def __unicode__(self):
        return self.fname


class PhotoGallery(models.Model):
    guid = models.AutoField(primary_key=True)
    memorial_guid = models.IntegerField()
    photoname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'photogallery'

    def __unicode__(self):
        return self.photoname


class ResetPwd(models.Model):
    emailid = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'resetpwd'

    def __unicode__(self):
        return self.emailid


class VideoGallery(models.Model):
    guid = models.AutoField(primary_key=True)
    memorial_guid = models.IntegerField()
    videoname = models.CharField(max_length=100)
    videolocation = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'videogallery'

    def __unicode__(self):
        return self.videoname
