from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    gender = models.CharField(max_length=6, blank= True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)


class AcademicsInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    roll_number = models.CharField(max_length=7, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)

class CompanyInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    salary = models.FloatField(blank=True)