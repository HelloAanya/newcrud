from django.db import models




class Employees(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    total_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, null=True, blank=True)
    available = models.BooleanField(default=True)   # Make it optional

    def __str__(self):
        return self.name





class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    service = models.CharField(max_length=100, default='Default Service')
     # Assuming Service is the correct related model

