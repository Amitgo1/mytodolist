from django.db import models

# Create your models here.
class MyToDo(models.Model):
    username = models.CharField(max_length=500)
    active = models.BooleanField(default=False)
