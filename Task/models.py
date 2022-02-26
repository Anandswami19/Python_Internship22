from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    

    class Meta():
        db_table = "task"    
