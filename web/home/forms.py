from django import forms
from .models import Note

class NoteFrom(forms.ModelForm):
    class Meta:
        model = Note
        fields  = "__all__"