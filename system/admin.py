from django.contrib import admin
from .models import Doctor, Patient,Opinion,Describe

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Describe)
admin.site.register(Opinion)
