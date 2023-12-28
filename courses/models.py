# models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    youtube_link = models.URLField()
    why_this_course = models.TextField()
    topics1 = models.TextField()
    topics2 = models.TextField()
    topics3 = models.TextField()
    topics4 = models.TextField()
    topics5 = models.TextField()
    topics6 = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    courses_image = models.ImageField(blank=True, upload_to='courses_images/')
    case1 = models.TextField()
    case2 = models.TextField()
    case3 = models.TextField()
    case4 = models.TextField()
    case5 = models.TextField()
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    name3 = models.CharField(max_length=100)
    name4 = models.CharField(max_length=100)
    name5 = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CourseTopic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
