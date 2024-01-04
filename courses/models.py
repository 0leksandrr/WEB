# models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    courses_image = models.ImageField(blank=True, upload_to='courses_images/')

    def __str__(self):
        return self.name

class CourseTopic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
