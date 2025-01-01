from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=15)
    Lname = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    contacts = models.CharField(max_length=15)
    email_address = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.Fname} {self.Lname}"

class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateTimeField()
    appointment_type = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.appointment_type

class Employee(models.Model):
    JOB_TITLES = [
        ('Gardener', 'Gardener'),
        ('Maintenance Technician', 'Maintenance Technician'),
        ('Horticulturist', 'Horticulturist'),
    ]

    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    contacts = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    job_title = models.CharField(max_length=100, choices=JOB_TITLES)
    hire_date = models.DateField()
    employment_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Supplies(models.Model):
    equipment_name = models.CharField(max_length=15)
    employees = models.ManyToManyField(Employee)
    description = models.TextField()

    def __str__(self):
        return self.equipment_name

class Service(models.Model):
    SERVICE_TYPES = [
        ('Maintenance', 'Maintenance'),
        ('Gardening', 'Gardening'),
        ('Consultation', 'Consultation'),
    ]
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    service_description = models.TextField()
    service_duration = models.DurationField()
    service_cost = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.service_type