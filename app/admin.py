from django.contrib import admin
from .models import Customer, Appointment, Employee, Supplies, Service
# Register your models here.
admin.site.register(Customer)
admin.site.register(Appointment)
admin.site.register(Employee)
admin.site.register(Supplies)
admin.site.register(Service)