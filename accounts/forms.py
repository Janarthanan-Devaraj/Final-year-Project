from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import User, AcademicsInfo, CompanyInfo

class UserAccountCreationForm(UserCreationForm):
        
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'dob', 'gender', 'password1', 'password2']
        widgets = {
            'dob':  forms.DateInput(attrs={'type': 'date'})
        }

class UserAcademicInfoCreationForm(ModelForm):
    
    roll_number = forms.CharField(max_length=7, error_messages={
        'unique': 'This roll number has already been registered.'
    })
    class Meta:
        model = AcademicsInfo
        fields = '__all__'
        exclude = ['user']


class UserCompanyInfoCreationForm(ModelForm):
    class Meta:
        model = CompanyInfo
        fields = '__all__'
        exclude = ['user']