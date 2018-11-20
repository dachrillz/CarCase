from django.conf.urls import url

#import views
from .views import Profile, UserViewSet

urlpatterns = [

    #register new users
    url(r'^signup/$', UserViewSet.as_view(), name='user_view_set'),

    #Employees
    url(r'$', Profile.as_view(), name='profile'),
]

