from django.urls import path
from Backend import views

urlpatterns = [
    path('', views.adminloginfun, name="adminloginfun"),
    path('adminloginpagefun/', views.adminloginpagefun, name="adminloginpagefun"),
    path('indexfun/', views.indexfun, name="indexfun"),
    path('adddepartment/', views.adddepartment, name="adddepartment"),
    path('departmentdbsave/', views.departmentdbsave, name="departmentdbsave"),
    path('displaydepartmentdata/', views.displaydepartmentdata, name="displaydepartmentdata"),
    path('editdepartment/<int:dataid>', views.editdepartment, name="editdepartment"),
    path('updatedepartment/<int:dataid>', views.updatedepartment, name="updatedepartment"),
    path('deldepartment/<int:dataid>', views.deldepartment, name="deldepartment"),
    path('adddoctors/', views.adddoctors, name="adddoctors"),
    path('doctordbsave/', views.doctordbsave, name="doctordbsave"),
    path('displaydoctorsdata/', views.displaydoctorsdata, name="displaydoctorsdata"),
    path('editdoctor/<int:dataid>', views.editdoctor, name="editdoctor"),
    path('updatedoctor/<int:dataid>', views.updatedoctor, name="updatedoctor"),
    path('deldoctor/<int:dataid>', views.deldoctor, name="deldoctor"),
    path('adminlogoutfun/', views.adminlogoutfun, name="adminlogoutfun"),
    path('superadminloginpage/', views.superadminloginpage, name="superadminloginpage"),
    path('superadminloginfun/', views.superadminloginfun, name="superadminloginfun"),
    path('superadminlogoutfun/', views.superadminlogoutfun, name="superadminlogoutfun"),
    path('appointmentdetails/', views.appointmentdetails, name="appointmentdetails"),
    path('adddtimeslot/', views.adddtimeslot, name="adddtimeslot"),
    path('timeslotdbsave/', views.timeslotdbsave, name="timeslotdbsave"),
    path('displattimeslot/', views.displattimeslot, name="displattimeslot"),
    path('deltimeslot/<int:dataid>', views.deltimeslot, name="deltimeslot"),
    # path('send_email/', views.send_email, name="send_email")

]

