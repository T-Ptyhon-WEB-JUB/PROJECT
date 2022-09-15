from django.db import models

# Create your models here.


class resumes(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=180)
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
