from django.db import models

# Create your models here.
class UserPoint(models.Model):
    payer = models.CharField(max_length=200)
    points = models.IntegerField
    timestamp = models.DateField

