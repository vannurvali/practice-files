from django.db import models

# Create your models here.


class Sample(models.Model):
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
    pic = models.FileField(upload_to='static/images')
