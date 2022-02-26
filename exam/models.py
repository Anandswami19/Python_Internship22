from django.db import models
from telnetlib import STATUS

# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.BooleanField(default=True)

    class Meta():
        db_table = 'exam'