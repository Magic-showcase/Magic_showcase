from django import forms

class Formularios_questions(forms.Form):

    asunto=forms.CharField()

    email=forms.EmailField()

    mensaje= forms.CharField()