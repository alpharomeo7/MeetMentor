from django import forms

class ChangesForm(forms.Form):
    preferred_name = forms.CharField(max_length=100)



    number = forms.CharField(max_length=20)

    expertise_1 = forms.CharField(max_length=20)
    expertise_2 = forms.CharField(max_length=20)
    expertise_3 = forms.CharField(max_length=20)
    expertise_4 = forms.CharField(max_length=20)
    expertise_5 = forms.CharField(max_length=20)
    expertise_6 = forms.CharField(max_length=20)

    profile_picture = forms.ImageField(required=False)


