from django.db import models

# Create your models here.


class resumes(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=180)
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='images/', default='static/images/images.png')
    pdf = models.FileField(
        upload_to='pdfs/', default='static/images/no_pdf.png')
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
