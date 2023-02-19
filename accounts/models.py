from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=7, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)


class AcademicsInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    roll_number = models.CharField(max_length=7, blank=True, unique=True)
    degree = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)

class CompanyInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    salary = models.BigIntegerField(blank=True)
    