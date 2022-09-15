from unicodedata import name
from . import models
from django import forms

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = ['title','content','image','author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__' #to include all fields

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control', 'id':'form2Example1','name':'username' }),
            'id':forms.TextInput(attrs={'class':'form-control', 'id':'form2Example2','name':'id' }),
            'email':forms.EmailInput(attrs={'class':'form-control', 'id':'form2Example3','name':'email' }),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'id':'form2Example4','name':'password' }),
        }

        labels={
            'username':'User Name',
            'id':'ID',
            'email':'Email',
            'password':'Password',
        }

        help_texts={
            'username':'Enter your user name',
            'id':'Enter your id',
            'email':'Enter your email',
            'password':'Enter your password',
        }

        error_messages={
            'username':{
                'max_length':'User name is too long',
                'required':'User name is required',
            },
            'id':{
                'max_length':'ID is too long',
                'required':'ID is required',
            },
            'email':{
                'max_length':'Email is too long',
                'required':'Email is required',
            },
            'password':{
                'max_length':'Password is too long',
                'required':'Password is required',
            },
        }
         