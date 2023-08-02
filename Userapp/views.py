from django.shortcuts import render, redirect, HttpResponse
from Userapp.models import Appointment, Signup
from Backend.models import Departmentdb, Doctorsdb
from django.contrib.auth.decorators import login_required


# For HomePage
def home(request):
    dep_data1 = Departmentdb.objects.all()
    return render(request, "home.html", {"dep_data1": dep_data1})


# OTP for New Password setting
# def otpVerify(request, uid):
#     if request.method == "POST":
#         profile = Profile.objects.get(uid=uid)
#         if request.COOKIES.get('can_otp_enter') != None:
#             if (profile.otp == request.POST['otp']):
#                 red = redirect("home")
#                 red.set_cookie('verified', True)
#                 return red
#             return HttpResponse("wrong otp")
#         return HttpResponse("10 minutes passed")
#     return render(request, "otp.html", {'id': uid})



# For to Make appointment for Users
@login_required(login_url='/')
def appointmentfun(request):
    dep_data2 = Departmentdb.objects.all()
    doc_data1 = Doctorsdb.objects.all()
    return render(request, "Appointment.html", {"doc_data1": doc_data1, "dep_data2": dep_data2})
def appointementdatasave(request):
    if request.method == "POST":
        nam = request.POST.get("name")
        dep = request.POST.get("department")
        doc = request.POST.get("doctor")
        dat = request.POST.get("date")
        tim = request.POST.get("time")
        num = request.POST.get("number")
        ema = request.POST.get("email")
        pla = request.POST.get("place")
        obj = Appointment(Name=nam, Department=dep, Doctor=doc, Date=dat, Time=tim, PhoneNumber=num, Place=pla, Email=ema)
        obj.save()
        return redirect(home)



# Display Doctor details for users
def doctorpage(request):
    doc_data2 = Doctorsdb.objects.all()
    return render(request, "doctors.html", {"doc_data2": doc_data2})




# Users signup and login
def signupsave(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        passw = request.POST.get("password")
        obj = Signup(Name=name, Email=email, Password=passw)
        obj.save()
        return redirect(home)

def userlogin(request):
    if request.method == "POST":
        username_d = request.POST.get("username")
        password_d = request.POST.get("password")
        if Signup.objects.filter(Name=username_d, Password=password_d).exists():
            request.session['username'] = username_d
            request.session['password'] = password_d
            return redirect(home)
        else:
            return redirect(home)
    else:
        return redirect(home)

def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(home)

def loginfun(request):
    return render(request, "login.html")


