from django import forms

class SetupForm(forms.Form):
    preferred_name = forms.CharField(max_length=100)

    gender = forms.CharField(max_length=10)

    number = forms.CharField(max_length=20)

    interest_1 = forms.CharField( max_length=20)
    interest_2 = forms.CharField( max_length=20)
    interest_3 = forms.CharField( max_length=20)
    interest_4 = forms.CharField(max_length=20)
    interest_5 = forms.CharField(max_length=20)
    interest_6 = forms.CharField(max_length=20)

    profile_picture = forms.ImageField(required = False)

    verification_code = forms.CharField(max_length=6)


class ChangesForm(forms.Form):
    preferred_name = forms.CharField(max_length=100)



    number = forms.CharField(max_length=20)

    interest_1 = forms.CharField(max_length=20)
    interest_2 = forms.CharField(max_length=20)
    interest_3 = forms.CharField(max_length=20)
    interest_4 = forms.CharField(max_length=20)
    interest_5 = forms.CharField(max_length=20)
    interest_6 = forms.CharField(max_length=20)

    profile_picture = forms.ImageField(required=False)


