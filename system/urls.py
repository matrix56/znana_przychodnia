from django.conf.urls import url
from . import views

app_name = 'system'

urlpatterns = [
    url(r'^$', views.opinion_list, name='homepage'),

    url(r'^register_doctor/$', views.register_doctor, name='rejestracja_lekarz'),

    url(r'^register_patient/$', views.register_patient, name='rejestracja_pacjent'),

    url(r'^login/$', views.login_user, name='logowanie'),

    url(r'^logout_user/$', views.logout_user, name='wylogowanie'),

    url(r'^doctor_list/$', views.doctor_list, name='doctor_list'),

    url(r'^calendar/$', views.add_calendar, name='dodaj_terminarz'),

    url(r'^opinion/$', views.add_opinion, name='dodaj_opinie'),

    url(r'^patient/$', views.patient_info, name='pacjent_info'),

    url(r'^question/$', views.add_question, name='zadaj_pytanie'),

    url(r'^opinion/(?P<pk>[0-9]+)/$', views.opinion_detail, name='opis_opinii'),

    url(r'^question/(?P<pk>[0-9]+)/$', views.question_detail, name='opis_pytania'),
]