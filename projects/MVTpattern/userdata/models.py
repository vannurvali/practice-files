from django.db import models

# Create your models here.


class Userdata(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)