from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime
# from colleges.models import Colleges
# from schools.models import Schools
from accounts.models import Signups

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

  userID = models.ForeignKey(Signups, on_delete=models.CASCADE)
  addteacherID = models.AutoField(primary_key=True)
  firstName = models.CharField(max_length = 15)
  lastName = models.CharField(max_length = 15)
  instituteType = models.CharField(max_length = 15, choices = INSTITUTE_TYPE)
  # if instituteType == 'School' :
    # instituteId = models.ForeignKey(Schools, on_delete=models.CASCADE)
  # else :
    # instituteId = models.ForeignKey(Colleges, on_delete = models.DO_NOTHING)
  institute = models.CharField(max_length = 50, choices = INSTITUTE)
  subjects = MultiSelectField(choices = SUBJECTS)
  age = models.IntegerField(default = 23)
  expirence = models.CharField(choices = EXPIRENCE, max_length = 50)
  # image = models.ImageField(upload_to = 'photos/teachers/addteachers', blank = True)
  moto = models.TextField()
  # datetime = models.DateTimeField(default = datetime.now())
  datetime = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.firstName + ' ' + self.lastName

