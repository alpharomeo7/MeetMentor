from django.shortcuts import render
from mentee.models import Mentee
from mentor.models import Mentor
from.models import Mentoring
from .forms import MentoringForm

from django.db.models import Q
from user.models import User
# Create your views here.
def mentoring(request,id=0) :

    user = request.user
    user1 = request.user
    if user.isMentee :
        user_client = Mentee.objects.get(user = user)
        ids  = user_client.connected_mentors.split()
    else :
        user_client = Mentor.objects.get(user=user)
        ids = user_client.connected_mentees.split()

    clients = []
    for client_id in ids :
        if user.isMentee :
         client = Mentor.objects.get(id = client_id)
        else :
            client = Mentee.objects.get(id = client_id)
        clients.append(client)
    if user.isMentee:
      chosen_client = Mentor.objects.get(id = ids[id])
    else :
      chosen_client = Mentee.objects.get(id=ids[id])

    print(chosen_client)
    mentorings = Mentoring.objects.filter(Q(sender = user1 , reciever = chosen_client.user) | Q(sender = chosen_client.user , reciever = user1 ))
    print(mentorings)


    if request.method == "GET":
        return render(request,'Chat.html',{'clients':clients,'chosen_client':chosen_client ,'mentorings':mentorings})
    else :
        new_mentoring = Mentoring(sender = request.user, )
        form = MentoringForm(request.POST)
        if form.is_valid() :

             reciever = User.objects.get(email=form.cleaned_data['reciever'])
             new_mentoring.reciever = reciever
             new_mentoring.message = form.cleaned_data['message']
             new_mentoring.save()
        request.method = "GET"
        return mentoring(request,id)




