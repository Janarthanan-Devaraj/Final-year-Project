from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import User, CompanyInfo, AcademicsInfo
from django.contrib.auth.decorators import login_required
from .forms import UserAccountCreationForm, UserAcademicInfoCreationForm, UserCompanyInfoCreationForm, EditUserAccount
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "accounts/index.html", {})

def profileView(request, pk):

    user = User.objects.get(username = pk)
    academics = AcademicsInfo.objects.get(user = user)
    company = CompanyInfo.objects.get(user = user)

    context = { 'user' : user, 'academics' : academics, 'company' : company }
    return render(request, "accounts/profile.html", context)

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

@login_required(login_url = 'login')
def editProfile(request):
    user = request.user
    academics = AcademicsInfo.objects.get(user = user)
    company = CompanyInfo.objects.get(user = user)
    form1 = EditUserAccount(instance = user)
    form2 = UserAcademicInfoCreationForm(instance = academics)
    form3 = UserCompanyInfoCreationForm(instance = company)

    if request.method == 'POST':
        form1 = EditUserAccount(request.POST, request.FILES, instance = user)
        form2 = UserAcademicInfoCreationForm(request.POST, request.FILES, instance = academics)
        form3 = UserCompanyInfoCreationForm(request.POST, request.FILES, instance = company)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form_userInfo = form1.save(commit=False)
            form_userInfo.user = request.user
            form_userInfo.save()
            form_academicInfo = form2.save(commit=False)
            form_academicInfo.user = request.user
            form_academicInfo.save()
            form_companyInfo = form3.save(commit=False)
            form_companyInfo.user = request.user
            form_companyInfo.save()
            

            return redirect('profile', pk = user.username)
    
    context = {'form1': form1, 'form2': form2, 'form3' : form3 }
    return render(request, 'accounts/edit-profile.html', context)


