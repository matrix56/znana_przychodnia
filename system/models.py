from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' +self.surname


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=9)


    def __str__(self):
        return self.name + ' ' + self.surname

class Pytanie(models.Model):
    autor = models.ForeignKey(Patient,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Opinion(models.Model):
    author = models.ForeignKey(Patient,on_delete=models.CASCADE)
    lekarz = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    opis = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Doctor.name + Doctor.surname

