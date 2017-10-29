from django.contrib.auth.models import User
from .models import Doctor,Patient
from django import forms

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password','email']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name','surname','specialization']

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['name', 'surname','pesel']