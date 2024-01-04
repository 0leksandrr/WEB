from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artiles(models.Model):
    title = models.CharField('Назва', max_length=250)
    full_text = models.TextField('Стаття')
    date = models.DateTimeField('Дата публікування')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
