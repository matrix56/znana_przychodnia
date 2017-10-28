from django.conf.urls import url
from . import views

app_name = 'system'

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),

    url(r'^register/$', views.UserFormView.as_view(), name='UserFormView'),

    url(r'^login/$', views.login_user, name='logowanie'),

    url(r'^doctor_list/$', views.doctor_list, name='doctor_list')
]