from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)  # ← Changed from specialization
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    availability = models.CharField(max_length=200, blank=True, null=True)  # ← Added

    def __str__(self):
        return self.name