from django import forms
from .models import *


class AddResumeForm(forms.ModelForm):
    class Meta:
        model = resumes
        fields = '__all__'
