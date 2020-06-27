from django import forms
from django.core import validators

def starts_with(value):
    if(value[0].lower!='d'):
        raise forms.ValidationError('name starts with d or D')

class Student(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    roll=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    branch=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    college=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
