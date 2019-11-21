from django.db import models
from django.utils import timezone
# Create your models here.
from user.models import User

class Mentoring(models.Model) :
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name= 'sender')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=3000,default ="This is a message")
    sent_at = models.DateTimeField(default= timezone.now)