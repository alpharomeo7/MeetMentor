from django.contrib import admin

# Register your models here.
from .models import Mentee, Interest

admin.site.register(Mentee)
admin.site.register(Interest)

