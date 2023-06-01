from django.db import models
from django import forms

# Create your models here.

class Person(models.Model) :
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    salary = models.FloatField()
    
class PersonForm(forms.ModelForm):
    class Meta :
        model = Person
        fields = '__all__'
        labels = {
            'first_name' : 'ชื่อ',
            'last_name' : 'นามสกุล',
            'salary' : 'เงินเดือน',
            
        }