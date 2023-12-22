from django.db import models

# Create your models here.
class Artiles(models.Model):
    title = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Стаття')
    date = models.DateTimeField('Дата публікування')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
