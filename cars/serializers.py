
from rest_framework import serializers
from .models import Employee,Car,Sales

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'brand', 'model', 'price', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = ('id', 'employee_id', 'carmodel_id', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
