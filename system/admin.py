from django.contrib import admin
from .models import Doctor, Patient, Opinion,Pytanie


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Opinion)
admin.site.register(Pytanie)
