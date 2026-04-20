from django.db import models

# Create your models here.
class Doctor(models.Model):
      name = models.CharField(max_length=200)
      specialization = models.CharField(max_length=200)
      phone = models.CharField(max_length=15)
      email = models.EmailField()

def __str__(self):
    return self.name