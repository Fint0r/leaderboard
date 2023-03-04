from django.db import models

# Create your models here.


class Employee(models.Model):
    """
    - name
    - role
    - picture
    - points

    """
    name = models.CharField(max_length=256)
    role = models.CharField(max_length=256)
    picture_location = models.CharField(max_length=256)
    points = models.IntegerField()
