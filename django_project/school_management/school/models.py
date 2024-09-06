from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    address = models.TextField()
    email = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
