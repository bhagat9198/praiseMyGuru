from django.db import models
from multiselectfield import MultiSelectField
from addTeacher.models import AddTeacher
from datetime import datetime
from django.db.models import Avg
from accounts.models import Signups


# Create your models here.
class Colleges(models.Model):
  CTYPE = (
    ('enginering','enginering'),
    ('law', 'law'),
    ('arts','arts')
  )
  userID = models.ForeignKey(Signups, on_delete=models.CASCADE)
  cid = models.AutoField(primary_key=True)
  cname = models.CharField(max_length = 50)
  ctype = MultiSelectField(choices = CTYPE)
  # totalTeachers = Teachers.id.count()
  # for ele in range(1,totalteachers)
  # cteachers = models.IntegerField(AddTeacher.objects.filter(id= cid).count())
  clocation = models.CharField(max_length = 150)
  cfounded = models.IntegerField()
  cwebsite = models.CharField(max_length = 50)
  # cteachersRating = models.IntegerField(Teacher.objects.aggregate(Avg(AddTeacher.objects.filter(id=cid))))
  cdatetime = models.DateTimeField(default = datetime.now())
  def __str__(self):
    return self.cname
