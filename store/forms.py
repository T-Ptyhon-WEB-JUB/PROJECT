# create a django form for the note model

from django import forms
from .models import ListedBook


class BookForm(forms.ModelForm):
    class Meta:
        model = ListedBook
        fields = '__all__'
