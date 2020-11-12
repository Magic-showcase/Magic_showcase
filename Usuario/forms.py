from django import forms

class Perilmodi(forms.Form):

    Photo = forms.ImageField()
    #country = forms.CharField(max_length=60, required=False) 
    #biografia = forms.CharField(max_length=500,required=False)