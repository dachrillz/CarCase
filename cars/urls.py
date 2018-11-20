from django.conf.urls import url

#import views
from .views import CreateCarView, CreateEmployeeView, CreateSalesView
from .views import EmployeeDetailView, CarDetailView, SalesViewDetail, TotalSalesView

urlpatterns = [
    #Employees
    url(r'employees/$', CreateEmployeeView.as_view(), name='employee'),
    url(r'employees/(?P<pk>[0-9]+)/$', EmployeeDetailView.as_view(), name='employee detail'),

    #Cars
    url(r'carmodels/$', CreateCarView.as_view(), name='carmodels'),
    url(r'carmodels/(?P<pk>[0-9]+)/$', CarDetailView.as_view(), name='car detail'),

    #Sales
    url(r'single_sales/', CreateSalesView.as_view(), name='sales'),
    url(r'single_sales/(?P<pk>[0-9]+)/$', SalesViewDetail.as_view(), name='sales detail'),

    #Total Sales
    url(r'total_sales/', TotalSalesView.as_view(), name='total_sales'),
]
