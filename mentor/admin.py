from django.contrib import admin

# Register your models herfrom
from .models import Mentor,Expertise

admin.site.register(Mentor)
admin.site.register(Expertise)