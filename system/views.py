from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Doctor,Opinion
from .forms import UserForm
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


class UserFormView(View):
    form_class = UserForm
    template_name = 'system/registration_form.html'

    #powrót do pustej formatki

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # dodanie nowego konta do bazy danych
    def post(self, request):
        form = self.form_class(request.POST or None)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # sprawdzenie poprawnosci dzialania
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('system:homepage')

        return render(request, self.template_name, {'form': form})