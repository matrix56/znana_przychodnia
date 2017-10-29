from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from django.db import models



class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' +self.surname + ' ' + self.specialization


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    pesel = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.surname
# Create your models here.
