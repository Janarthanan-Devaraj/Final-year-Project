from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import User, CompanyInfo, AcademicsInfo
from .forms import UserAccountCreationForm, UserAcademicInfoCreationForm, UserCompanyInfoCreationForm
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    return render(request, "accounts/index.html",{'user': user})

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

def signupPage1(request):
    form = UserAccountCreationForm()

    if request.method == 'POST':
        form = UserAccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            authenticate(request, username = user.username, password = user.password)
            login(request, user)
            return redirect('signup-step2')
        else:
            messages.error(request, 'An error occurred during registration')
    
    context = {'form' : form}
    return render(request, 'accounts/signup_step1.html', context)

def signupPage2(request):
    form = UserAcademicInfoCreationForm()

    if request.method == 'POST':
        form = UserAcademicInfoCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('signup-step3')
        else:
            messages.error(request, 'An error occurred during registration')
    
    context = {'form' : form}
    return render(request, 'accounts/signup_step2.html', context)

def signupPage3(request):
    form = UserCompanyInfoCreationForm()

    if request.method == 'POST':
        form = UserCompanyInfoCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('index')
        else:
            messages.error(request, 'An error occurred during registration')
    
    context = {'form' : form}
    return render(request, 'accounts/signup_step3.html', context)

