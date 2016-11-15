# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Documentgallery(models.Model):
    guid = models.AutoField(primary_key=True)
    memorial_guid = models.IntegerField()
    documentname = models.CharField(max_length=100)
    documentlocation = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'documentgallery'


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


class Photogallery(models.Model):
    guid = models.AutoField(primary_key=True)
    memorial_guid = models.IntegerField()
    photoname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'photogallery'


class Resetpwd(models.Model):
    emailid = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'resetpwd'


class Videogallery(models.Model):
    guid = models.AutoField(primary_key=True)
    memorial_guid = models.IntegerField()
    videoname = models.CharField(max_length=100)
    videolocation = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'videogallery'
