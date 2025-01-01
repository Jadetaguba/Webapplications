from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, CustomerListView, AppointmentListView, EmployeeListView, ServiceListView, SuppliesListView, CustomerDetailView, AppointmentDetailView, EmployeeDetailView, ServiceDetailView, SuppliesDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('customer', CustomerListView.as_view(), name='customer'),
    path('appointment', AppointmentListView.as_view(), name='appointment'),
    path('employee', EmployeeListView.as_view(), name='employee'),
    path('service', ServiceListView.as_view(), name='service'),
    path('supplies', SuppliesListView.as_view(), name='supplies'),
    path('customer/<int:pk>', CustomerDetailView.as_view(), name='customer_detail'),
    path('appointment/<int:pk>', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('employee/<int:pk>', EmployeeDetailView.as_view(), name='employee_detail'),
    path('service/<int:pk>', ServiceDetailView.as_view(), name='service_detail'),
    path('supplies/<int:pk>', SuppliesDetailView.as_view(), name='supplies_detail'),
]