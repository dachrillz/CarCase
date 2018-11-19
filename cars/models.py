from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


class Car(models.Model):
    brand = models.CharField(max_length=255, blank=False, unique=True)
    model = models.CharField(max_length=255, blank=False, unique=True)
    price = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

class Sales(models.Model):
    employee_id = models.CharField(max_length=255, blank=False, unique=False)
    carmodel_id= models.CharField(max_length=255, blank=False, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
