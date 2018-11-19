from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .models import Employee, Car, Sales
from .serializers import EmployeeSerializer, CarSerializer, SalesSerializer, TotalSalesSerializer
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

class CreateSalesView(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

    def perform_create(self, serializer):
        serializer.save()


    def get(self, *arg, **kwargs):

        to_be_serialized = {}

        local_sales = Sales.objects.all()
        local_sales = list(local_sales)

        for item in local_sales:

            personid = item.employee_id

            emp_name = Employee.objects.get(id=int(personid)).name

            car_price = Car.objects.get(id=int(item.carmodel_id)).price

            if emp_name not in to_be_serialized:
                to_be_serialized[personid] = [int(car_price),emp_name]
            else:
                to_be_serialized[personid][0] += int(car_price)

        # create instance of model
        serializer_instance = TotalSalesSerializer(data = {'data': to_be_serialized})
        if serializer_instance.is_valid():
            serializer_instance.save()
            status_code=201
        return Response(serializer_instance.data, status=status_code)


