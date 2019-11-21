from django import forms

class MentoringForm(forms.Form):


    reciever = forms.CharField( max_length= 300)
    message = forms.CharField( max_length= 3000)
