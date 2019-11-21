"""MeetMentor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from mentee.views import setup
from django.contrib import admin

from mentee.views import homepage
import user.urls

# Register the admin views or call admin.autodiscover()


from user.views import  landing_page
from user.views import login_view , logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(user.urls)),

    path('home/',include('mentee.urls'),name = 'home'),
                  path('mentor/', include('mentor.urls'), name='home'),
    path('setup/',setup),
    path('logout/',logout_view),
    path('mentoring/',include('mentoring.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)