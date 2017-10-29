from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Doctor
from .forms import UserForm, DoctorForm,PatientForm
from django.db import transaction
# Create your views here.


def homepage(request):
    return render(request, 'system/homepage.html')


def doctor_list(request):
    list = Doctor.objects.all().order_by('name')
    return render(request, 'system/doctor_list.html', {'list': list})


def doctor_detail(request, pk):
    list = get_object_or_404(Doctor, pk=pk)
    return render(request, "system/doctor_detail.html", {'list': list})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'system/logout.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'system/homepage.html',)
            else:
                return render(request, 'system/login.html', {'error_message': 'Konto zablokowane'})
        else:
            return render(request, 'system/login.html', {'error_message': 'Błędne logowanie'})

    return render(request, 'system/login.html')

@transaction.atomic
def register_doctor(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST or None)
        doctor_form = DoctorForm(request.POST or None)

        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = doctor_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request,user)
            return render(request,'system/homepage.html')
        else:
            return render(request, 'system/registration_form.html', {'error_message': 'Konto zablokowane'})
    else:
        user_form = UserForm()
        doctor_form = DoctorForm()

    return render(request,
            'system/registration_form.html',
            {'user_form': user_form, 'doctor_form': doctor_form, 'registered': registered} )

@transaction.atomic
def register_patient(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST or None)
        patient_form = PatientForm(request.POST or None)

        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = patient_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            return render(request, 'system/registration_patient.html', {'error_message': 'Konto zablokowane'})
    else:
        user_form = UserForm()
        patient_form = PatientForm()

    return render(request,
            'system/registration_patient.html',
            {'user_form': user_form, 'patient_form': patient_form, 'registered': registered} )
