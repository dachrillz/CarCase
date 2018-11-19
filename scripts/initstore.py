import json
import requests
from pprint import pprint


json_data = open('data.json').read()

json_data = json.loads(json_data)

URL       = 'http://127.0.0.1:8000'
URL_EMP   = URL + '/api/employees/'
URL_CARS  = URL + '/api/carmodels/'
URL_SALES = URL + '/api/total_sales/'

headers = {
    "content-type": "application/json"
}

#Employees
emp = json_data['carshop']['employees']

#Create the employees through post requests
for employee in emp:
    name = employee['name']

    PARAM = {'name' : name}

    r = requests.post(url = URL_EMP, headers = headers, json = PARAM)

    print(r)


#Cars
cars = json_data['carshop']['carmodels']
for car in cars:
    brand = car['brand']
    model = car['model']
    price = car['price']

    PARAM = {'brand' : brand, 'model' : model, 'price' : price}
    r = requests.post(url = URL_CARS, headers = headers, json = PARAM)

    print(r)

#Sales
sales = json_data['carshop']['sales']
for sale in sales:
    emp_id = sale['employee_id']
    car_id = sale['carmodel_id']

    PARAM = {'employee_id' : emp_id, 'carmodel_id' : car_id}
    r = requests.post(url = URL_SALES, headers = headers, json = PARAM)

    print(r)
