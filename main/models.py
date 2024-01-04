from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.IntegerField()
    image = models.ImageField(blank=True, upload_to = 'teachers/')

    def __str__(self):
        return self.name