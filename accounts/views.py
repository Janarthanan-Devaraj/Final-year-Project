from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import User, CompanyInfo, AcademicsInfo
from .forms import UserAccountCreationForm, UserAcademicInfoCreationForm, UserCompanyInfoCreationForm
from django.contrib import messages


def index(request):
    return render(request, "accounts/index.html",{})

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.object.get(username = username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username = username, password = password)


        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'Username or password is incorrect!!!')

    return render(request, 'accounts/login.html',{})

def logoutPage(request):
    logout(request)
    return redirect('login')
# Create your views here.
