# from django.db import models
# from multiselectfield import MultiSelectField
# # from addTeacher.models import AddTeacher
# from accounts.models import Signups
# from datetime import datetime


# # Create your models here.
# class Praise(models.Model):
#   STARS = (
#     ('1','1'),
#     ('2','2'),
#     ('3','3'),
#     ('4','4'),
#     ('5','5'),
#   )
#   SUBJECTS = (
#     ('civil', 'civil'),
#     ('compuer organization', 'compuer organization'),
#     ('data structures', 'data structures'),
#     ('mathematics','mathematics'),
#     ('chemistry','chemistry'),
#     ('electrical','electrical'),
#     ('at&c','at&c'),
#     ('networking','networking'),
#     ('dotnet','dotnet'),
#     ('software engineering','software engineering'),
#     ('algorthiums','algorthiums'),
#     ('c','c'),
#     ('physics','physics'),
#     ('mechnical','mechnical'),
#     ('electronics','electronics'),
#     ('java','java'),
#     ('management fot it','management fot it'),
#     ('dbms','dbms'),
#   )
#   TAGS = (
#     ('Respected','Respected'),
#     ('Gives Homework','Gives Homework'),
#     ('Accessible Outside Class','Accessible Outside Class'),
#     ('Participation Matters','Participation Matters'),
#     ('Can Skip Class Easily','Can Skip Class Easily'),
#     ('Fluttershy','Fluttershy'),
#     ('Inspirational','Inspirational'),
#     ('Test Heavy','Test Heavy'),
#     ('Group Projects','Group Projects'),
#     ('Clear Grading Criteria','Clear Grading Criteria'),
#     ('Hilarious','Hilarious'),
#     ('Beware Of Pop Quizzers','Beware Of Pop Quizzers'),
#     ('Amazing Lectures','Amazing Lectures'),
#     ('Lecture Heavy','Lecture Heavy'),
#     ('Caring','Caring'),
#     ('Extra Credit','Extra Credit'),
#     ('Tough Grader','Tough Grader'),
#     ('Have to write notes','Have to write notes'),
#   )
#   SUGGEST = (
#     ('yes','yes'),
#     ('no','no'),
#   )
#   # teacherID = models.IntegerField(primary_key=True, auto_increment = True)
#   userID = models.ForeignKey(Signups, on_delete = models.DO_NOTHING )
#   # addteacherID = models.ForeignKey(AddTeacher, on_delete = models.DO_NOTHING)
#   teacherID = models.AutoField(primary_key=True)
#   worthListening = models.IntegerField()
#   starts = models.CharField(max_length = 1, choices = STARS)
#   subjects = MultiSelectField(choices = SUBJECTS)
#   tags = MultiSelectField(choices = TAGS)
#   suggest = models.CharField(max_length = 1, choices = SUGGEST)
#   suggestion = models.TextField()
#   datetime = models.DateTimeField(default = datetime.now())
#   def __str__(self):
#     return self.teacherID