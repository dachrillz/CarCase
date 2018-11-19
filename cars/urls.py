from django.conf.urls import url

#import views
from .views import CreateCarView, CreateEmployeeView

urlpatterns = [
    url(r'employees/$', CreateEmployeeView.as_view(), name='employee'),
    url(r'carmodels/$', CreateCarView.as_view(), name='carmodels'),
    #url(r'total_sales/$', TotalSales.as_view(), name='total_sales'),
]
