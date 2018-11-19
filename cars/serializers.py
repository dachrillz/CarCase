
from rest_framework import serializers
from .models import Employee,Car

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'name', 'sales', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
