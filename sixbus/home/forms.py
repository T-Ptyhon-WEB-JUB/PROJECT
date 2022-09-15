from django import forms
from .models import bus1
from .models import bus2

class addressForm1(forms.ModelForm):
    class Meta:
        model = bus1
        fields = "__all__"



class addressForm2(forms.ModelForm):
    class Meta:
         model = bus2
         fields = "__all__"