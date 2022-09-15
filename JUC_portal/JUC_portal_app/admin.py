from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Student)
admin.site.register(models.BlogPost)
admin.site.register(models.Community)
admin.site.register(models.News_Post)

