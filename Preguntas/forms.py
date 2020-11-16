from django import forms

class Formularios_questions(forms.Form):

    asunto=forms.CharField(required="true")

    email=forms.EmailField(required="true")

    mensaje= forms.CharField(required="true")