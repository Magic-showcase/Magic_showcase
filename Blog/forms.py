from django import forms
class FormularioBlog(forms.Form):

    Titulo=forms.CharField()
    Contenido=forms.CharField()
    Imagen=forms.ImageField()
    Autor=forms.CharField()
    Categorias=forms.CharField()