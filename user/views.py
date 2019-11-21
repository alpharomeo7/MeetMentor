from django.shortcuts import render
from .models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import RegistrationForm
from .forms import LoginForm, ChangePasswordForm
"""


from .forms import ContactUsForm
from .forms import ForgotPasswordEmailForm
from .forms import ForgotPasswordForm
"""
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.db import IntegrityError
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
import random
import string
# Create your views here.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def landing_page(request) :
    return render(request, 'user/landing_page.html')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def login_view (request) :
    if request.method ==  "GET" :
        return render(request, 'user/login.html')

    else :
            print(request.POST)
            if 'name' in request.POST:
                form = RegistrationForm(request.POST)
                error = False

                if form.is_valid():
                    print("VALIIDDD")
                    email = form.cleaned_data['email']
                    password = form.cleaned_data['password']
                    confirm_password = form.cleaned_data['confirm_password']
                    name = form.cleaned_data['name']

                    if len(password) >= 8 and password == confirm_password:
                        try:
                            user = User.objects.create_user(email, password)
                        except IntegrityError as e:
                            print("OK HERE")
                            error = True
                            message = 'Email Already exists'
                            print(message)
                            return render(request, 'user/login.html',
                                          {'register_name': name, 'register_email': email, 'message': message})
                        else:
                            user.name = form.cleaned_data['name']
                            user.save()

                            message = 'Account created'
                            print(message)
                            return render(request, 'user/login.html',
                                          {'register_name': name, 'register_email': email, 'message': message})


                    else:
                        form.cleaned_data['password'] = ''
                        form.cleaned_data['confirm_password'] = ''
                        form = RegistrationForm(initial=form.cleaned_data)

                        error = True
                        message = 'Passwords do not match. Ensure that you type the SAME password in Confirm Password and  contain at least 8 charcters'
                        print(message)
                        return render(request, 'user/login.html',
                                      {'register_name': name, 'register_email': email,'message' : message})


            else:
                form = LoginForm(request.POST)
                if form.is_valid():
                    email = form.cleaned_data['email']
                    password = form.cleaned_data['password']
                    user = authenticate(email=email, password=password)
                    if user is not None:
                        print(email + ' ' + password)
                        login(request, user)

                        if user.isMentee :
                         return HttpResponseRedirect('/home')
                        else :
                         return HttpResponseRedirect('/mentor/home')

                    else:
                        print('opps')

                return render(request, 'user/login.html',{'message' : 'Incorrect Username or Password'})
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')
def change_password_view(request) :
    if request.method == "GET"  :
      return  render(request,'user/change_password.html')
    else :
        print(request.POST)
        form = ChangePasswordForm(request.POST)
        if form.is_valid() :
             if request.user.check_password(form.cleaned_data['old_password'])  :
                 if len(form.cleaned_data['new_password']) >= 8 :


                     if form.cleaned_data['confirm_new_password'] == form.cleaned_data['new_password'] :
                         request.user.set_password(form.cleaned_data['new_password'])
                         request.user.save()
                         return render(request, 'user/change_password.html' , {'success' : 'Yay'})
                     else :
                        return render(request, 'user/change_password.html' , {'error' : 'New and Confirm Password DO not match'})
                 else :
                     return render(request, 'user/change_password.html',
                                   {'error': 'New Password should be of atleast 8 characters'})
             else:
               return render(request, 'user/change_password.html', {'error': 'Incorrect Old Passsword'})

        else:
               return render(request, 'user/change_password.html', {'error': 'Invalid form'})
def about(request) :
    return render(request, 'user/about.html')

