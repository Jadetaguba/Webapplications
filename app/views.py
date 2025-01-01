from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Customer, Appointment, Employee, Service, Supplies
class HomePageView(TemplateView):
    template_name ='app/home.html'

class AboutPageView(TemplateView):
    template_name ='app/about.html'

class ContactPageView(TemplateView):
    template_name ='app/contact.html'

class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'app/Customer_lists.html'

class AppointmentListView(ListView):
    model = Appointment
    context_object_name = 'appointments'
    template_name = 'app/Appointments_lists.html'

class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'app/Employees_lists.html'

class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = 'app/Services_lists.html'

class SuppliesListView(ListView):
    model = Supplies
    context_object_name = 'supplies'
    template_name = 'app/Supplies_lists.html'

class CustomerDetailView(DetailView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'app/Customers_detail.html'

class AppointmentDetailView(DetailView):
    model = Appointment
    context_object_name = 'appointments'
    template_name = 'app/Appointment_detail.html'

class EmployeeDetailView(DetailView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'app/Employee_detail.html'

class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'services'
    template_name = 'app/Services_detail.html'

class SuppliesDetailView(DetailView):
    model = Supplies
    context_object_name = 'supplies'
    template_name = 'app/Supplies_detail.html'