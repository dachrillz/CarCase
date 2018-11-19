from django.conf.urls import url

#import views
from .views import CreateCarView, CreateEmployeeView, CreateSalesView

urlpatterns = [
    url(r'employees/', CreateEmployeeView.as_view(), name='employee'),
    url(r'carmodels/', CreateCarView.as_view(), name='carmodels'),
    url(r'total_sales/$', CreateSalesView.as_view(), name='total_sales'),
]
