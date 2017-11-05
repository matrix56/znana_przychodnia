from django.contrib.auth.models import User
from pip._vendor.ipaddress import AddressValueError

from .models import Doctor,Patient,Opinion,Question
from schedule.models import Event,Calendar
from django import forms

class UserForm(forms.ModelForm):

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

class CalendarForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title','description','start','creator']

class OpinionForm(forms.ModelForm):

    class Meta:
        model = Opinion
        fields = ['title','text']

class QuestionForm(forms.ModelForm):
    title = forms.CharField(widget=Doctor)
    class Meta:
        model = Question
        fields = ['title','text']
