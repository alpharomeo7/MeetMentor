from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
import string
import random
# Create your models here.





class UserManager(BaseUserManager) :
       def create_user(self, email , password = None ):
           user = self.model(email = self.normalize_email(email))
           user.set_password(password)

           user.username  = user.email
           user.forgot_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
           user.verification_code  = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
           user.isMentee = True
           user.save(using=self._db)
           return user
       def create_superuser(self, email , password = None):
            user  = self.create_user(email, password = None)

            user.is_superuser = True
            user.is_staff = True
            return user



class User(AbstractUser) :

    email = models.EmailField(max_length = 255 , unique = True)
    USERNAME_FIELD = 'email'
    active = models.BooleanField(default = False  )
    isMentor = models.BooleanField(default=False)
    isMentee = models.BooleanField(default=False)
    REQUIRED_FIELDS = []
    forgot_code = models.CharField(default= "random", max_length = 6)
    name = models.CharField(default= "Name", max_length = 200)
    objects  = UserManager()
    verification_code = models.CharField(default="123456", max_length=511)




    def __str__(self):
        return self.email




