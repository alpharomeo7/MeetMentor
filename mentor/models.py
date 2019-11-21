from django.db import models
from user.models import User

# Create your models here.
# Create your models here.

class Expertise(models.Model):
    title  = models.CharField(max_length = 322)
    code  = models.CharField(max_length = 32)




class Mentor(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  preferred_name = models.CharField(max_length = 32)
  expertises = models.CharField(max_length = 100)
  gender = models.CharField(max_length=10,default = 'other')
  number = models.CharField(max_length=20, default='0')
  profile_picture = models.ImageField(default= 'default.png' , blank = True)
  bio = models.CharField(max_length=300, default = "none")
  connected_mentees = models.CharField(max_length=200, default=' ')
  def __str__(self):
        return self.name
