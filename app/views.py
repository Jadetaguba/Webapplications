from contextlib import suppress

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Customer, Appointment, Employee, Service, Supplies
from django.urls import reverse_lazy
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
    template_name = 'app/Employees_detail.html'

class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'services'
    template_name = 'app/Services_detail.html'

class SuppliesDetailView(DetailView):
    model = Supplies
    context_object_name = 'supplies'
    template_name = 'app/Supplies_detail.html'

class CustomerCreateView(CreateView):
    model = Customer
    fields = ['customer_id', 'Fname', 'Lname', 'gender', 'contacts', 'email_address']
    template_name = 'app/Customer_create.html'

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['customer', 'appointment_date', 'appointment_type', 'notes', 'location']
    template_name = 'app/Appointments_create.html'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = [ 'employee_id', 'first_name', 'last_name', 'gender', 'contacts', 'email', 'job_title', 'hire_date', 'employment_type']
    template_name = 'app/Employees_create.html'

class ServicesCreateView(CreateView):
    model = Service
    fields = ['service_type', 'service_description', 'service_duration', 'service_cost', 'frequency', 'status']
    template_name = 'app/Services_create.html'

class SuppliesCreateView(CreateView):
    model = Supplies
    fields = ['equipment_name', 'employees', 'description']
    template_name = 'app/Supplies_create.html'

class CustomerUpdateView(UpdateView):
    model = Customer
    context_object_name = 'cust'
    fields = ['customer_id', 'Fname', 'Lname', 'gender', 'contacts', 'email_address']
    template_name = 'app/Customer_update.html'

class AppointmentUpdateView(UpdateView):
    model = Appointment
    context_object_name = 'app'
    fields = ['customer', 'appointment_date', 'appointment_type', 'notes', 'location']
    template_name = 'app/Appointments_update.html'

class EmployeeUpdateView(UpdateView):
    model = Employee
    context_object_name = 'emp'
    fields = ['employee_id', 'first_name', 'last_name', 'gender', 'contacts', 'email', 'job_title', 'hire_date', 'employment_type']
    template_name = 'app/Employees_update.html'

class ServicesUpdateView(UpdateView):
    model = Service
    context_object_name = 'serv'
    fields = ['service_type', 'service_description', 'service_duration', 'service_cost', 'frequency', 'status']
    template_name = 'app/Services_update.html'

class SuppliesUpdateView(UpdateView):
    model = Supplies
    context_object_name = 'supp'
    fields = ['equipment_name', 'employees', 'description']
    template_name = 'app/Supplies_update.html'

class CustomerDeleteView(DeleteView):
    model = Customer
    context_object_name = 'cust'
    template_name = 'app/Customer_delete.html'
    success_url = reverse_lazy('customer')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    context_object_name = 'app'
    template_name = 'app/Appointments_delete.html'
    success_url = reverse_lazy('appointment')

class EmployeeDeleteView(DeleteView):
    model = Employee
    context_object_name = 'emp'
    template_name = 'app/Employees_delete.html'
    success_url = reverse_lazy('employee')

class ServicesDeleteView(DeleteView):
    model = Service
    context_object_name = 'serv'
    template_name = 'app/Services_delete.html'
    success_url = reverse_lazy('services')

class SuppliesDeleteView(DeleteView):
    model = Supplies
    context_object_name = 'supp'
    template_name = 'app/Suppllies_delete.html'
    success_url = reverse_lazy('supplies')
