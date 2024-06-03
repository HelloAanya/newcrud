from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.models import Employees
from django.utils import timezone
from .forms import EmployeesForm, BookingForm


def HomePage(request):
    emp = Employees.objects.all()
    context = {'emp': emp}
    return render(request, 'home.html', context)

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = User.objects.create_user(uname, email, password)
        my_user.save()
        return redirect('login')
    return render(request, 'signup.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid username or password")
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, redirect
from app.models import Employees

def HomePage(request):
    emp = Employees.objects.all()
    context = {
        'emp': emp,
    }
    return render(request, 'home.html', context)

def Add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')  
        total_time = request.POST.get('total_time')
        address = request.POST.get('address')  # Get address from the POST data
        created_at = timezone.now()  
        available = request.POST.get('available') == 'True'  
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        emp = Employees.objects.create(
            name=name,
            description=description,  
            total_time=total_time,
            address=address,  # Include address in the create() method
            created_at=created_at,
            available=available,
            email=email,
            phone=phone,
        )

    return redirect('home')

def Edit(request):
    emp = Employees.objects.all()
    context = {
        'emp': emp,
    }
    return render(request, 'edit.html', context)

def Update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        total_time = request.POST.get('total_time')
        available = request.POST.get('available')

        emp = Employees.objects.get(id=id)
        emp.name = name
        emp.description = description
        emp.total_time = total_time
        emp.available = available
        emp.save()

    return redirect('home')



def Delete(request, id):
    emp = Employees.objects.get(id=id)
    emp.delete()
    return redirect('home')

def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the admin interface
    else:
        form = BookingForm()
    return render(request, 'book_service.html', {'form': form})

def home(request):
    available_services = Booking.objects.filter(available=True)
    not_available_services = Booking.objects.filter(available=False)
    context = {
        'available_services': available_services,
        'not_available_services': not_available_services,
    }
    return render(request, 'home.html', context)
