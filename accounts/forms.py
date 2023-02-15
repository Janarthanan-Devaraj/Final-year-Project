from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, AcademicsInfo, CompanyInfo

class UserAccountCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'age', 'gender', 'password1', 'password2']

class UserAcademicInfoCreationForm(ModelForm):
    class Meta:
        model = AcademicsInfo
        fields = '__all__'
        exclude = ['user']

class UserCompanyInfoCreationForm(ModelForm):
    class Meta:
        model = CompanyInfo
        fields = '__all__'
        exclude = ['user']