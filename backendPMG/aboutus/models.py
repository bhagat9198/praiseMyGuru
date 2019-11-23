from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Feedback(models.Model) :
  EXPIRENCE = (
    ('Best','Best'),
    ('Good','Good'),
    ('Worst', 'Worst')
  )

  HELP = (
    ('Yes','Yes'),
    ('No', 'No'),
  )

  CATEGORIES = (
    ('Student','Student'),
    ('Guru','Guru'),
    ('Other profession', 'Other profession')
  )
  name = models.CharField(max_length=20)
  email = models.EmailField(max_length = 20)
  exp = models.CharField(max_length = 20, choices=EXPIRENCE)
  helpp = models.CharField(max_length = 20, choices = HELP)
  category = models.CharField(max_length = 20, choices = CATEGORIES)
  suggestion = models.CharField(max_length = 1000)
  dateTime = models.DateTimeField(timezone.now())

  def __str__(self) :
    return self.email
