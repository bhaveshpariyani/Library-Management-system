from django import forms
from django.forms import ModelForm
from .models import Books

class BooksForms(ModelForm):
    class Meta:
        model = Books
        fields = "__all__"  #("list of fiels")

        labels={
            'name':'',
            'ISBN':'',
            'quantity':'',
            'author':'',
            'pages':'',
            'description':''
        }
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Book Name'}),
            'ISBN':forms.TextInput(attrs={'class':'form-control','placeholder':'ISBN number'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'Quantity'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Author Name'}),
            'pages':forms.NumberInput(attrs={'class':'form-control','placeholder':'No of Pages'}),
            'description':forms.TextInput(attrs={'class':'form-control','placeholder':'Description'})
        }
