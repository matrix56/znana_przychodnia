from django.contrib.auth.models import User
from pip._vendor.ipaddress import AddressValueError
from django.forms import extras
from .models import Doctor,Patient,Opinion,Pytanie,Terms
from django import forms
from django.utils import timezone
from django import forms
from captcha.fields import ReCaptchaField




class UserForm(forms.ModelForm):
    captcha = ReCaptchaField()
    password = forms.CharField(widget=forms.PasswordInput,min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Błędne hasło"
            )

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ['name','surname','specialization']


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['name', 'surname', 'phone_number']



class OpinionForm(forms.ModelForm):

    class Meta:
        model = Opinion
        fields = ['lekarz','opis']

class PytanieForm(forms.ModelForm):

    class Meta:
        model = Pytanie
        fields = ['title','text']

class TermForm(forms.ModelForm):
    data = forms.DateField(widget=extras.SelectDateWidget)
    czas = forms.TimeField(initial=timezone.now())
    class Meta:
        model = Terms
        fields = ['data','czas']
