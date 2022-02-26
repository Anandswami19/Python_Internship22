from msilib.schema import Class
from django.db import models

class Hr(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Conatct=models.IntegerField()


    class Meta():
        db_table : 'Hr'
