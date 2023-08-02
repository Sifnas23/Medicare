from django.urls import path
from Userapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('appointmentfun/', views.appointmentfun, name="appointmentfun"),
    path('appointementdatasave/', views.appointementdatasave, name="appointementdatasave"),
    path('doctorpage/', views.doctorpage, name="doctorpage"),
    path('signupsave/', views.signupsave, name="signupsave"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('loginfun/', views.loginfun, name="loginfun"),
    # path('otp/<str:uid>/', views.otpVerify, name='otp')
]