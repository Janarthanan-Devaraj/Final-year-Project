from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('signup/step1/', views.signupPage1, name="signup-step1"),
    path('signup/step2/', views.signupPage2, name="signup-step2"),
    path('signup/step3/', views.signupPage3, name="signup-step3"),
    path('profile/<str:pk>/',views.profileView, name="profile"),
    path('edit-profile/',views.editProfile, name="edit-profile"),
]