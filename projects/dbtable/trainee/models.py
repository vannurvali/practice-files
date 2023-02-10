from django.db import models

# Create your models here.


class Trainee(models.Model):
    name = models.CharField(max_length=100)
    reg_id = models.IntegerField()
    phone_number = models.BigIntegerField()
    subject = models.CharField(max_length=50)