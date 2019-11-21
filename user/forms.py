from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField( max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'eg. name@email.com'}))
    password = forms.CharField( max_length=16,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Anything more secrue than password123'}))
    confirm_password = forms.CharField(max_length=16,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'The same password you wrote in Password'}))

class LoginForm(forms.Form) :
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg. name@email.com'}))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'your password'}))
class ChangePasswordForm(forms.Form) :
    old_password = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'your password'}))
    new_password = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'your password'}))
    confirm_new_password = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'your password'}))