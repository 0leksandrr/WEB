from django.db import models

class PDFFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdf_files/')