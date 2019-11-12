from django.db import models
from django import forms
from datetime import datetime

# Create your models here.

class Signups(models.Model):
  CHOICES = (
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
  )
  firstName = models.CharField(max_length = 15)
  lastName = models.CharField(max_length = 15)
  userName = models.CharField(max_length = 15)
  email = models.EmailField(max_length = 15)
  password = models.CharField(max_length = 15)
  confirmPassword = models.CharField(max_length = 15)
  category = models.CharField(choices = CHOICES, max_length = 10)
  agreeTerms = models.BooleanField(default = True)
  dateTime = models.DateTimeField(default = datetime.now())
  def __str__(self):
    return self.userName