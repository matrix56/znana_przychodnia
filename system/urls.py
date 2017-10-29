from django.conf.urls import url
from . import views

app_name = 'system'

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),

    url(r'^register_doctor/$', views.register_doctor, name='rejestracja_lekarz'),

    url(r'^register_patient/$', views.register_patient, name='rejestracja_pacjent'),

    url(r'^login/$', views.login_user, name='logowanie'),

    url(r'^logout_user/$', views.logout_user, name='wylogowanie'),

    url(r'^doctor_list/$', views.doctor_list, name='doctor_list')
]