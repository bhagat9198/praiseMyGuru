from django.db import models
from django import forms
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Signups(models.Model):
  CHOICES = (
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
  )
  # id = models.AutoField(primary_key=True)
  firstName = models.CharField(max_length = 15)
  lastName = models.CharField(max_length = 15)
  userName = models.CharField(max_length = 15)
  email = models.EmailField(max_length = 50)
  password = models.CharField(max_length = 15)
  confirmPassword = models.CharField(max_length = 15)
  category = models.CharField(choices = CHOICES, max_length = 10)
  agreeTerms = models.BooleanField(default = True)
  dateTime = models.DateTimeField(timezone.now())
  
  def __str__(self):
    return self.userName


class Dashbord(models.Model) :
  id = models.AutoField(primary_key=True)
  userID = models.ForeignKey(Signups, on_delete = models.DO_NOTHING)
  status = models.CharField(max_length = 9999)
  image = models.ImageField(upload_to = 'media/post', blank = True, null = True)
  dateTime = models.DateTimeField(timezone.now())

  def __str__(self) :
    return self.userID

