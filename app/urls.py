from django.urls import path
from .views import (HomePageView, AboutPageView, ContactPageView, CustomerListView, AppointmentListView,
                    EmployeeListView, ServiceListView, SuppliesListView, CustomerDetailView,
                    AppointmentDetailView, EmployeeDetailView, ServiceDetailView, SuppliesDetailView,
                    CustomerCreateView, AppointmentCreateView, EmployeeCreateView, ServicesCreateView,
                    SuppliesCreateView, CustomerUpdateView, AppointmentUpdateView, EmployeeUpdateView,
                    ServicesUpdateView, SuppliesUpdateView, CustomerDeleteView, AppointmentDeleteView,
                    EmployeeDeleteView, ServicesDeleteView, SuppliesDeleteView)

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
    path('customer/create', CustomerCreateView.as_view(), name='customer_create'),
    path('appointment/create', AppointmentCreateView.as_view(), name='appointment_create'),
    path('employee/create', EmployeeCreateView.as_view(), name='employee_create'),
    path('service/create', ServicesCreateView.as_view(), name='service_create'),
    path('supplies/create', SuppliesCreateView.as_view(), name='supplies_create'),
    path('customer/<int:pk>/edit', CustomerUpdateView.as_view(), name='customer_update'),
    path('appointment/<int:pk>/edit', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('employee/<int:pk>/edit', EmployeeUpdateView.as_view(), name='employee_update'),
    path('service/<int:pk>/edit', ServicesUpdateView.as_view(), name='service_update'),
    path('supplies/<int:pk>/edit', SuppliesUpdateView.as_view(), name='supplies_update'),
    path('customer/<int:pk>/delete', CustomerDeleteView.as_view(), name='customer_delete'),
    path('appointment/<int:pk>/delete', AppointmentDeleteView.as_view(), name='appointment_delete'),
    path('employee/<int:pk>/delete', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('service/<int:pk>/delete', ServicesDeleteView.as_view(), name='service_delete'),
    path('supplies/<int:pk>/delete', SuppliesDeleteView.as_view(), name = 'supplies_delete')
]

