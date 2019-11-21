from django.db import models
from user.models import User
# Create your models here.
class Interest(models.Model):
    title  = models.CharField(max_length = 322)
    code  = models.CharField(max_length = 32)

    def __str__(self):
        return self.title


class Mentee(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=62)
  preferred_name = models.CharField(max_length = 32)
  interests = models.CharField(max_length = 555)
  gender = models.CharField(max_length=10, default='other')
  number = models.CharField(max_length=20, default='0')
  profile_picture = models.ImageField(default= 'default.png' , blank = True)
  connected_mentors = models.CharField(max_length=200, default=' ')
  def __str__(self):
        return self.name
