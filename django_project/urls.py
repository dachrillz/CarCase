"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.views import generic

#Swagger
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='API SCHEMA')

#Authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/$', generic.RedirectView.as_view(url='/docs/', permanent=False)), #Redirect to documentation
    url(r'^docs/$', schema_view),

    #Apps
    url(r'^api/', include('cars.urls')),

    #Authentication
    url(r'^$', generic.RedirectView.as_view(url='auth/login/?next=/api/', permanent=False)), #Redirect to login screen
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/token/obtain/$', TokenObtainPairView.as_view()),
    url(r'^auth/token/refresh/$', TokenRefreshView.as_view()),

    #Get profile view when logged in as user
    url(r'^profile/', include('user.urls')),

]
