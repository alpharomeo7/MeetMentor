from django.shortcuts import render
from mentee.models import Interest, Mentee
from.models import Mentor
from django.http import HttpResponseRedirect

# Create your views here.

def homepage(request)  :


    if request.method == "GET" :
        try :
            print('STAGE 0')

            user = request.user
            mentor = Mentor.objects.get(user = user)

            expertises = mentor.expertises
            expertises = expertises.split()
            print('STAGE 1')
            expertise_0 = ''
            expertise_1 = ''
            expertise_2 = ''
            expertise_3 = ''
            expertise_4 = ''
            expertise_5 = ''
            if len(expertises) > 0  :
                expertise_0 = Interest.objects.get(code=expertises[0])

            if len(expertises) > 1  :
                expertise_1 =  Interest.objects.get(code=expertises[1])
            if len(expertises) > 2  :
                expertise_2 = Interest.objects.get(code=expertises[2])
            if len(expertises) > 3 :
                expertise_3 =  Interest.objects.get(code=expertises[3])
            if len(expertises) > 4  :
                expertise_4 =  Interest.objects.get(code=expertises[4])
            if len(expertises) > 5  :
                expertise_5 = Interest.objects.get(code=expertises[5])



            connected_mentees = []

            connected_mentees_id = mentor.connected_mentees
            connected_mentees_id = connected_mentees_id.split()

            print(connected_mentees_id)
            if len(connected_mentees_id) > 0 :
                    for id in connected_mentees_id :

                        connected_mentees.append(Mentee.objects.get(id= id))
            print(connected_mentees)





            return render(request,'mentor/homepage.html',{'mentor': mentor,'expertise_0': expertise_0 ,
                                                          'expertise_1': expertise_1,
                                                          'expertise_2': expertise_2,
                                                          'expertise_3': expertise_3,
                                                          'expertise_4': expertise_4,
                                                          'expertise_5': expertise_5 ,
                                                          'connected_mentees' : connected_mentees,
                                                          'len_of_connected_mentees' : len(connected_mentees)

                                                          })
        except :
            return HttpResponseRedirect('setup')
        
        