from django import forms
from .models import Employees, Booking  # Import the Booking model

class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['name', 'description', 'total_time', 'available', 'address', 'email', 'phone']  # Include additional fields from the Employees model



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'contact_email', 'location', 'date', 'service']
