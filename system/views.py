from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Doctor,Opinion,Patient,Pytanie
from .forms import UserForm, DoctorForm,PatientForm,OpinionForm,PytanieForm
from django.db import transaction
from django.utils import timezone
# Create your views here.

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


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

def opinion_detail(request,pk):
    opinions = get_object_or_404(Opinion, pk=pk)
    return render(request, 'system/opinion_detail.html', {'opinions': opinions})

def add_opinion(request):
    if request.method == "POST":
        form = OpinionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.patient
            post.published_date = timezone.now()
            post.save()
            return redirect('system:opis_opinii', pk=post.pk)
    else:
        form = OpinionForm()
    return render(request, 'system/add_opinion.html', {'form': form})

def question_detail(request,pk):
    questions = get_object_or_404(Pytanie, pk=pk)
    return render(request, 'system/question_detail.html', {'questions': questions})

def add_question(request):
    if request.method == "POST":
        form = PytanieForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user.patient
            post.published_date = timezone.now()
            post.save()
            return redirect('system:opis_pytania', pk=post.pk)
    else:
        form = PytanieForm()
    return render(request, 'system/add_question.html', {'form': form})

def opinion_list(request):
    opinions = Opinion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,"system/homepage.html",{'opinions':opinions})

def question_list(request):
    questions = Pytanie.objects.all()
    return render(request,"system/homepage.html",{'questions':questions})

def patient_info(request):
    return render(request,"system/patient.html")

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
            return render(request, 'system/login.html', {'error_message': 'Konto nie istnieje'})

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
            return render(request, 'system/registration_form.html', {'error_message': 'Błedne logowanie'})
    else:
        user_form = UserForm()
        doctor_form = DoctorForm()
    return render(request,
            'system/registration_form.html',
            {'user_form': user_form, 'doctor_form': doctor_form, 'registered': registered} )

@transaction.atomic
def register_patient(request):
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
            login(request,user)
            return render(request,'system/homepage.html')
        else:
            return render(request, 'system/registration_patient.html', {'error_message': 'Niepoprawne dane'})
    else:
        user_form = UserForm()
        patient_form = PatientForm()

    return render(request,
            'system/registration_patient.html',
            {'user_form': user_form, 'patient_form': patient_form} )
"""
@transaction.atomic
def add_calendar(request):
    if request.method == "POST":
        calendar_form = EventForm(request.POST or None)

        if calendar_form.is_valid():
            calendar_form.save(commit= False)
        else:
            return render(request,'system/calendar_doctor.html',{'error_message' : 'Niepoprawny format danych'})

    else:
        calendar_form = EventForm()

        return render(request, 'system/calendar_doctor.html',{'calendar_form':calendar_form})
"""