'''
Serializers for the users app
'''

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    '''
    Serializer class for the User model
    '''
    class Meta:
        '''
        Meta class for User Serializer
        '''
        model = User
        fields = (
            'id',
            'name',
            'username',
            'password',
            'email',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
