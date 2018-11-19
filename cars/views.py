from django.shortcuts import render

from rest_framework import generics
from .models import Employee, Car
from .serializers import EmployeeSerializer, CarSerializer

# Create your views here.
#EmployeeList, CarModelList, TotalSales


class CreateEmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save()

class CreateCarView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save()
