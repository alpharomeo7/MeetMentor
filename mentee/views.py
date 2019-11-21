from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from .forms import SetupForm, ChangesForm
from .models import Mentee, Interest

from mentor.models import Mentor
# Create your views here.
def setup(request) :
    print (request.POST)
    if request.method == "GET" :
      return render(request, 'mentee/setup.html')
    else :
        form = SetupForm(request.POST,request.FILES or None)
        print("OKAY  MM")
        if form.is_valid() :
            print("HMM")
            mentee = Mentee(preferred_name = form.cleaned_data['preferred_name'],user = request.user)
            print(mentee.preferred_name)
            print(mentee.user)
            print(mentee.id)
            interests = ''
            interest = form.cleaned_data['interest_1']
            if interest not in interests and interest is not  'none' :
                interests = interests + ' ' +  interest

            interest = form.cleaned_data['interest_2']
            if interest not in interests and interest is not 'none':
                interests = interests + ' ' +  interest

            interest = form.cleaned_data['interest_3']
            if interest not in interests and interest is not 'none':
                interests = interests + ' ' +  interest
            interest = form.cleaned_data['interest_4']
            if interest not in interests and interest is not 'none':
                interests = interests + ' ' +  interest

            interest = form.cleaned_data['interest_5']
            if interest not in interests and interest is not 'none':
                interests = interests + ' ' +  interest

            interest = form.cleaned_data['interest_6']
            if interest not in interests and interest is not 'none':
                interests = interests + ' ' +  interest


            if mentee.user.verification_code == form.cleaned_data['verification_code'] :


                mentee.interests = interests
                mentee.name = request.user.name
                mentee.gender = form.cleaned_data['gender']
                if ( form.cleaned_data['profile_picture'] is not None) :
                 mentee.profile_picture = form.cleaned_data['profile_picture']
                mentee.save()
            else :
                return render(request, 'mentee/setup.html',{'error' : 'Incorrect Verification Code'})



        else  :
            return render(request, 'mentee/setup.html',{'form': form})

@login_required
def homepage(request)  :
    if  request.user.isMentee  != True:
        return HttpResponseRedirect('/mentor/home')
    if request.method == "GET" :

            print('STAGE 0')

            user = request.user
            try :
              mentee = Mentee.objects.get(user = user)
            except :
                return HttpResponseRedirect("setup")
            mentors = []

            interests = mentee.interests.replace('none','')
            interests = interests.split()
            mentors_q =[]
            print('STAGE 1')
            interest_0 = ''
            interest_1 = ''
            interest_2 = ''
            interest_3 = ''
            interest_4 = ''
            interest_5 = ''
            print(interests)
            if len(interests) > 0  :
                interest_0 = Interest.objects.get(code=interests[0])
            else:
                interest_0 = Interest.objects.get(code='none')
            if len(interests) > 1  :
                interest_1 =  Interest.objects.get(code=interests[1])
            if len(interests) > 2  :
                interest_2 = Interest.objects.get(code=interests[2])
            if len(interests) > 3 :
                interest_3 =  Interest.objects.get(code=interests[3])
            if len(interests) > 4  :
                interest_4 =  Interest.objects.get(code=interests[4])
            if len(interests) > 5  :
                interest_5 = Interest.objects.get(code=interests[5])
            for interest in interests:
                try :
                 mentors_q = Mentor.objects.filter(expertises__contains=interest)
                except :
                   a =1
                for i in range(len(mentors_q)):
                    mentors.append(mentors_q[i])
            print('STAGE 2')

            connected_mentors = []

            connected_mentors_id = mentee.connected_mentors
            connected_mentors_id = connected_mentors_id.split()
            print('STAGE 2.7')
            print((connected_mentors_id))

            if len(connected_mentors_id) > 0 :
                    for id in connected_mentors_id :
                       try :
                         connected_mentors.append(Mentor.objects.get(id= id))
                       except :
                           a =2
            print("hmmm")

            return render(request,'mentee/homepage.html',{'mentee': mentee,'mentors' : mentors,'interest_0': interest_0 ,
                                                          'interest_1': interest_1,
                                                          'interest_2': interest_2,
                                                          'interest_3': interest_3,
                                                          'interest_4': interest_4,
                                                          'interest_5': interest_5 ,
                                                          'connected_mentors' : connected_mentors,
                                                          'len_of_connected_mentors' : len(connected_mentors),
                                                          'len_mentors' : len(mentors),

                                                          })

    else :
        print(request.POST)

        user = request.user
        mentee = Mentee.objects.get(user=user)
        print ('BEFORE')
        print(mentee.connected_mentors)

        mentee.connected_mentors +=  ' '+str(request.POST['id'])
        mentor = Mentor.objects.get(id=request.POST['id'])

        mentor.connected_mentees += ' ' + str(mentee.id)
        mentor.save()

        print ('AFTEr')
        print(mentee.connected_mentors)
        mentee.save()

        return HttpResponseRedirect('/home')
def changes_view(request) :
    if request.method == "GET"  :
        user = request.user
        mentee = Mentee.objects.get(user=user)


        interests = mentee.interests

        interests = interests.split()
        print('STAGE 1')
        interest_0 = ''
        interest_1 = ''
        interest_2 = ''
        interest_3 = ''
        interest_4 = ''
        interest_5 = ''
        if len(interests) > 0:
            interest_0 = Interest.objects.get(code=interests[0])
        else:
            interest_0 = Interest.objects.get(code='none')
        if len(interests) > 1:
            interest_1 = Interest.objects.get(code=interests[1])
        else:
            interest_1 = Interest.objects.get(code='none')
        if len(interests) > 2:
            interest_2 = Interest.objects.get(code=interests[2])
        else:
            interest_2 = Interest.objects.get(code='none')
        if len(interests) > 3:
            interest_3 = Interest.objects.get(code=interests[3])
        else:
            interest_3= Interest.objects.get(code='none')
        if len(interests) > 4:
            interest_4 = Interest.objects.get(code=interests[4])
        else:
            interest_4 = Interest.objects.get(code='none')
        if len(interests) > 5:
            interest_5 = Interest.objects.get(code=interests[5])

        else:
            interest_5 = Interest.objects.get(code='none')
        return render(request, 'mentee/changes.html', {'mentee': mentee, 'interest_0': interest_0,
                                                        'interest_1': interest_1,
                                                        'interest_2': interest_2,
                                                        'interest_3': interest_3,
                                                        'interest_4': interest_4,
                                                        'interest_5': interest_5,

                                                        })
    else:
        form = ChangesForm(request.POST)
        print (request.POST,request.FILES or None )
        if form.is_valid() :

            mentee = Mentee.objects.get(user = request.user)
            print(mentee.preferred_name)

            interests = ''
            interest = form.cleaned_data['interest_1']
            if interest not in interests and interest is not 'none' :
                interests = interests + ' ' +  interest

            interest = form.cleaned_data['interest_2']
            if interest not in interests and interest is not 'none':
                interests = interests + ' ' +  interest

            interest = form.cleaned_data['interest_3']
            if interest not in interests and interest is not 'none':
                interests = interests + ' ' +  interest
            interest = form.cleaned_data['interest_4']
            if interest not in interests and interest is not 'none':
                interests = interests + ' ' +  interest

            interest = form.cleaned_data['interest_5']
            if interest not in interests and interest is not 'none':
                interests = interests + ' ' +  interest

            interest = form.cleaned_data['interest_6']
            if interest not in interests and interest is not 'none':
                interests = interests + ' ' +  interest
            print(interests)
            mentee.interests = interests.replace('none','')
            mentee.name = request.user.name
            mentee.number = form.cleaned_data['number']
            if ( form.cleaned_data['profile_picture'] is not None) :

             mentee.profile_picture = form.cleaned_data['profile_picture']
            mentee.save()
            return HttpResponseRedirect('/home')



        else  :
            print('not valid')
            return HttpResponseRedirect('/home')
















