from django import forms
from .models import Task
#to change or update
class TodoForms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']