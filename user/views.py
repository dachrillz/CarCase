
'''
Views for the 'users app'
'''
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model

from .models import User
from .serializers import UserSerializer

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

class UserViewSet(CreateAPIView):
    '''
    View class for creating new users
    '''

    model = get_user_model()
    permission_classes = [
        permissions.IsAdminUser # Only allow admins to register new people
    ]

    serializer_class = UserSerializer

class Profile(generics.RetrieveAPIView):

    def get(self, *args, **kwargs):
        instance = User.objects.get(id=self.request.user.id)
        serializer = UserSerializer(instance)
        return Response(serializer.data)

