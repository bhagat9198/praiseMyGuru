from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime
from django.db.models import Avg
from addTeacher.models import AddTeacher

# Create your models here.
class Schools(models.Model):
  STYPE = (
    ('kindergarten','kindergarten'),
    ('primary', 'primary'),
    ('highschool','highschool'),
    ('preuniversity','preuniversity')
  )

  sid = models.AutoField(primary_key=True)
  sname = models.CharField(max_length = 50)
  stype = MultiSelectField(choices = STYPE)
  # totalTeachers = Teachers.id.count()
  # for ele in range(1,totalteachers)
  # steachers = models.IntegerField(AddTeacher.objects.filter(id= cid).count())
  slocation = models.CharField(max_length = 150)
  sfounded = models.IntegerField()
  swebsite = models.CharField(max_length = 50)
  # steachersRating = models.IntegerField(Teacher.objects.aggregate(Avg(AddTeacher.objects.filter(id=cid))))
  sdatetime = models.DateTimeField(default = datetime.now())
  def __str__(self):
    return self.cname