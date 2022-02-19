from django.urls import path,include
from .views import thankyou,Apnmntsuccess,Bed,Home,Appnmnt, Upapview,Contact,about,Signup,Signup1,AdminLogin,StaffLogin,ActiveLogin,Pending_appointments,signout,Dtlapview,Deleteap
app_name="hospital"

urlpatterns = [
    path("",Home.as_view(),name='home'),
    path("about",about,name='about'),
    path("appointment",Appnmnt.as_view(),name='appointments'),
    path("contact",Contact.as_view(),name='contact'),
    path("signup",Signup.as_view(),name='register'),
    path("signup1",Signup1.as_view(),name='registeradmin'),
    path("login",ActiveLogin.as_view(),name='login'),
    path("AdminLogin",AdminLogin.as_view(),name='loginadmin'),
    path("StaffLogin",StaffLogin.as_view(),name='loginstaff'),
    path("Pending_appointments",Pending_appointments.as_view(),name='Editapnmnt'),
    path("signout",signout,name='logout'),
    path("Detailed_appointment/<int:pk>",Dtlapview.as_view(),name="dtlapview"),
    path("Edit_appointment/<int:pk>",Upapview.as_view(),name="edit_appointment"),
    path("Delete_appointment/<int:pk>",Deleteap.as_view(),name="deleteap"),
    path('success/<int:pk>',Apnmntsuccess.as_view(),name="apnmntsuccess"),
    path("Avilable_beds",Bed,name="bed"),
    path('Thankyou',thankyou,name="Thanks"),
    

] 