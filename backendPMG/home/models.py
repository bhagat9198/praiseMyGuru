from django.db import models
from django import forms
from multiselectfield import MultiSelectField

# Create your models here.
class Try(models.Model) :
  Colleges = (
    ('civil', 'civil'),
    ('compuer organization', 'compuer organization'),
    ('data structures', 'data structures'),
    ('mathematics','mathematics'),
    ('chemistry','chemistry'),
    ('electrical','electrical'),
    ('at&c','at&c'),
    ('networking','networking'),
    ('dotnet','dotnet'),
    ('software engineering','software engineering'),
    ('algorthiums','algorthiums'),
    ('c','c'),
    ('physics','physics'),
    ('mechnical','mechnical'),
    ('electronics','electronics'),
    ('java','java'),
    ('management fot it','management fot it'),
    ('dbms','dbms'),
  )
  name = models.CharField(max_length = 50)
  # sub = models.CharField(choices = SUBJECTS, max_length = 50)
  # sub = MultiSelectField(choices = SUBJECTS, max_length = 50)
  # drop = models.CharField(choices = Colleges, max_length = 50)
  # num = models.CharField(max_length = 50)
  # pic = models.FileField(upload_to='teachers/pics/')
  # exp = models.CharField(max_length = 50)
  txt = models.CharField(max_length = 500)
  def __str__(self):
        return self.name;
  