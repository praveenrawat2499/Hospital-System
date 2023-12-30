from django.shortcuts import render, redirect, get_object_or_404,redirect
from datetime import datetime
from appointment.models import Appointment
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from app.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as dj_login,logout as dj_logout,authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')
    
def appointment(request):
    return render(request, 'appointment.html')
    
def contact(request):
    return render(request, 'contact.html')
    
def service(request):
    return render(request, 'service.html')

def feature(request):
    return render(request, 'feature.html')

def Error_404(request):
    return render(request, '404.html')

def team(request):
    return render(request, 'team.html')
    
def testimonial(request):
    return render(request, 'testimonial.html')


# Appointment form 
def appointment_form(request):
    data = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        hospital = request.POST.get('hospital')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%m/%d/%Y').date() if date_str else None
        time_str = request.POST.get('time')

        try:
            # Parse time input as a string to be stored in the database
            time = datetime.strptime(time_str, '%I:%M %p').time() if time_str else None
        except ValueError:
            raise ValidationError(_('Invalid time format. It must be in HH:MM AM/PM format.'))
        
        description = request.POST.get('description')   
    
        appointment = Appointment(name = name, phone_no = phone_no, 
                                  email = email, hospital = hospital, department = department, doctor= doctor, 
                                  description = description, date = date, time = time)
        
        appointment.save()
        data = {"message": "your details has been submited"}
        # print(name, email, phone_no, doctor, date, time, description)
        print(request.POST)
    return render(request, "appointment.html", data)
    
   
def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] == cd['confirm_password']:
                obj = form.save(commit=False)
                obj.set_password(obj.password)
                obj.save()
                messages.success(request, 'You have been registered.')
                return redirect('index')

            else:
                return render(request, "registration.html", {'form':form,'note':'password must match'})

    else:
        form = RegistrationForm()

    return render(request, "registration.html", {'form':form})


def login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    

        if user is not None:
            dj_login(request,user)
            return redirect('dashboard')

        else:
            messages.success(request, 'Invalid username or password!')
            return render(request, "login.html")

    else:
        return render(request, "login.html")
    
@login_required
def custom_logout(request):
    dj_logout(request)
    return redirect('index')


@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(email=request.user.email)
    return render(request, 'appointment_list.html', {'appointments': appointments})
    