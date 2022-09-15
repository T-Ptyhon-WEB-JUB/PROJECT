from email.mime import image
from django.db import models
# from ckeditor.fields import RichTextField

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=50)
    id = models.CharField(max_length=50,primary_key=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # content = RichTextField(blnk=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Student,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    
    def __str__(self):
        return self.title
        

class News_Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    Post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Student,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',null=True,blank=True)

    
    def __str__(self):
        return self.title

class Community(models.Model):
    platforms = (
        ('whatsapp',('Whatsapp')),
        ('discord', ('Discord')),
        ('telegram', ('Telegram')),
    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    platform=models.CharField(max_length=50,choices=platforms)

    def __str__(self):
        return self.name