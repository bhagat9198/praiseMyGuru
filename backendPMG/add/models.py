from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
from datetime import datetime
from django.utils import timezone
# from colleges.models import Colleges
# from schools.models import Schools
from accounts.models import Signups
from django.contrib.auth.models import User 

# Create your models here.
class AddTeacher(models.Model):
  INSTITUTE_TYPE = (
    ('School', ' School'),
    ('College', 'College'),
  )
  SUBJECTS = (
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
  EXPIRENCE = (
    ('1yr', '1yr'),
    ('2yr', '2yr'),
    ('3yr', '3yr'),
    ('5yr', '5yr'),
    ('8yr', '8yr'),
    ('15yr', '15yr'),
    ('15plus', '15plus')
  )
  INSTITUTE = (
    ('svit', 'svit'),
    ('bmsit','bmsit'),
    ('presidency','presidency'),
    ('ramaiah','ramaiah')
  )

  # userID = models.ForeignKey(User, on_delete = models.CASCADE)
  userID = models.ForeignKey(Signups,null=True, blank=True, default='0', on_delete = models.CASCADE)
  addteacherID = models.AutoField(primary_key=True)
  firstName = models.CharField(max_length = 15)
  lastName = models.CharField(max_length = 15)
  instituteType = models.CharField(max_length = 15, choices = INSTITUTE_TYPE)
  # if instituteType == 'School' :
    # instituteId = models.ForeignKey(Schools, on_delete=models.CASCADE)
  # else :
    # instituteId = models.ForeignKey(Colleges, on_delete = models.DO_NOTHING)
  institute = models.CharField(max_length = 50, choices = INSTITUTE)
  subjects = MultiSelectField(choices = SUBJECTS, max_length = 50)
  age = models.IntegerField(default = 23)
  expirence = models.CharField(choices = EXPIRENCE, max_length = 50)
  image = models.ImageField(upload_to = 'media/media', blank = True, null = True)
  moto = models.CharField(max_length = 10000)
  dateTime = models.DateTimeField(timezone.now())

  def __str__(self):
    return self.firstName + ' ' + self.lastName


class AddCollege(models.Model) :
  TYPES = (
    ('Engineering','Engineering'),
    ('Law','Law'),
    ('Arts','Arts'),
    ('Commerce','Commmerce')
  )
  DESCRIBE = (
    ('Prestigious','Prestigious'),
    ('Decent','Decent'),
    ('Average','Average')
  )

  userID = models.ForeignKey(Signups,null=True, blank=True, default='0', on_delete = models.CASCADE)
  name = models.CharField(max_length = 20)
  location = models.CharField(max_length = 20)
  types = MultiSelectField(choices = TYPES)
  describe = models.CharField(max_length = 200, choices = DESCRIBE)
  website = models.CharField(max_length = 50)
  phone = models.IntegerField(max_length = 12)
  founded = models.IntegerField(max_length = 4)
  # image2 = models.ImageField(upload_to = 'media/colleges', blank = True)
  dateTime = models.DateTimeField(timezone.now())

  def __str__(self) :
    return self.name


class AddSchool(models.Model) :
  TYPES = (
    ('Kidargarden','Kidargarden'),
    ('Primary','Primary'),
    ('HighSChool','HighSChool'),
    ('PreUniversity','PreUniversity')
  )
  DESCRIBE = (
    ('Prestigious','Prestigious'),
    ('Decent','Decent'),
    ('Average','Average')
  )
  userID = models.ForeignKey(Signups,null=True, blank=True, default='0', on_delete = models.CASCADE)
  name = models.CharField(max_length = 20)
  location = models.CharField(max_length = 20)
  types = MultiSelectField(choices = TYPES)
  describe = models.CharField(max_length = 20, choices = DESCRIBE)
  website = models.CharField(max_length = 50)
  phone = models.IntegerField(max_length = 12)
  founded = models.IntegerField(max_length = 4)
  # image1 = models.ImageField(upload_to = 'media/media', blank = True)
  dateTime = models.DateTimeField(timezone.now())

  def __str__(self) :
    return self.name