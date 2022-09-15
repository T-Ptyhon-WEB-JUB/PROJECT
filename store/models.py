from django.db import models

# Create your models here.


class ListedBook(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/')
    contact_number = models.CharField(max_length=255)

    def __str__(self):
        return self.title
