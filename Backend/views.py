from django.shortcuts import render, redirect
from Backend.models import Admin, Departmentdb, Doctorsdb, TimeSlot
from Userapp.models import Appointment
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from .utils import send_email_to_client
from django.contrib.auth.decorators import login_required


def indexfun(request):
    return render(request, "index.html")


def adminloginpagefun(request):
    return render(request, "admin_login.html")
def adminloginfun(request):
    if request.method == "POST":
        username_d = request.POST.get("username")
        password_d = request.POST.get("password")
        if Admin.objects.filter(Email=username_d, Password=password_d).exists():
            request.session['username'] = username_d
            request.session['password'] = password_d
            return redirect(indexfun)
        else:
            return redirect(adminloginpagefun)
    else:
        return redirect(adminloginpagefun)


def adminlogoutfun(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminloginpagefun)

def adddepartment(request):
    return render(request, "adddepartment.html")

def departmentdbsave(request):
    if request.method == "POST":
        na = request.POST.get('department')
        de = request.POST.get('description')
        obj = Departmentdb(Name=na, Description=de)
        obj.save()
        return redirect(adddepartment)


def displaydepartmentdata(request):
    data = Departmentdb.objects.all()
    return render(request, "displaydepartmentdetails.html", {"data": data})


def editdepartment(request, dataid):
    data = Departmentdb.objects.get(id=dataid)
    print(data)
    return render(request, "Editdepartmentdetails.html", {"data": data})


def updatedepartment(request, dataid):
    if request.method == "POST":
        na = request.POST.get('department')
        de = request.POST.get('description')

        Departmentdb.objects.filter(id=dataid).update(Name=na, Description=de)
        return redirect(displaydepartmentdata)


def deldepartment(request, dataid):
    data = Departmentdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydepartmentdata)

def adddoctors(request):
    dep_data = Departmentdb.objects.all()
    return render(request, "adddoctorsdetails.html", {"dep_data": dep_data})


def doctordbsave(request):
    if request.method == "POST":
        nam = request.POST.get('doctor')
        dep = request.POST.get('department')
        qua = request.POST.get('qualification')
        im = request.FILES['image']
        obj = Doctorsdb(Name=nam, Department=dep, Qualification=qua,Image=im)
        obj.save()
        return redirect(adddoctors)


def displaydoctorsdata(request):
    data = Doctorsdb.objects.all()
    return render(request, "displaydoctordetails.html", {"data": data})


def editdoctor(request, dataid):
    data = Doctorsdb.objects.get(id=dataid)
    da = Departmentdb.objects.all()
    print(data)
    return render(request, "Editdoctorsdetails.html", {"data": data, "da": da})


def updatedoctor(request, dataid):
    if request.method == "POST":
        dep = request.POST.get('department')
        doc = request.POST.get('doctor')
        qua = request.POST.get('qualification')
        try:
            im = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = Doctorsdb.objects.get(id=dataid).Image
        Doctorsdb.objects.filter(id=dataid).update(Department=dep, Name=doc, Qualification=qua, Image=file)
        return redirect(displaydoctorsdata)


def deldoctor(request, dataid):
    data = Doctorsdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydoctorsdata)



# Superadmin backend_login functions

def superadminloginpage(request):
    return render(request, "superadmin_loginbackend.html")
def superadminloginfun(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(indexfun)
            else:
                return redirect(superadminloginpage)
        else:
            return redirect(adminloginpagefun)
def superadminlogoutfun(request):
    del request.session['username']
    del request.session['password']
    return redirect(superadminloginpage)

# Appoitmentdetails functions

def appointmentdetails(request):
    data = Appointment.objects.all()
    return render(request, "appointmentdetails.html", {"data": data})

# Email to Patient

# def send_email(request):
#     send_email_to_client
#     return redirect(indexfun)

def adddtimeslot(request):
    return render(request, "add_timeslot.html")

def timeslotdbsave(request):
    if request.method == "POST":
        day = request.POST.get('day')
        time = request.POST.get('time')
        doctor = request.POST.get('doctor')
        obj = TimeSlot(Day=day, Time=time,  Doctor=doctor)
        obj.save()
        return redirect(adddtimeslot)

def displattimeslot(request):
    data = TimeSlot.objects.all()
    return render(request, "displaytimeslot.html", {"data": data})


def deltimeslot(request, dataid):
    data = TimeSlot.objects.filter(id=dataid)
    data.delete()
    return redirect(displattimeslot)










