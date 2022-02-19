from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from .models import Appointment, Department, Contact,Beds
from django.views.generic import ListView,View,CreateView,DetailView,DeleteView,TemplateView
from django.contrib.auth import authenticate, login,logout
from .forms import Logform,Register
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse_lazy,reverse

# Create your views here.

'''def home(request):
    a=Department.objects.all()
    st=""
    return render(request,"hospital/home.html",{'data':a})'''

class Home(ListView):
    template_name='hospital\home.html'
    context_object_name='data'
    def get_queryset(self):
        return enumerate(Department.objects.all())
   
''''def contact(request): 
    if request.method =="POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        contact= Contact(name=name,email=email, phone=phone,date=datetime.today()) 
        contact.save()
        return HttpResponse('your contact information has been submitted succesfully.')
    return render(request,"hospital/contact.html") '''

class Contact(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'hospital/contact.html'
    def get_success_url(self):
        return reverse('hospital:Thanks')
    
def about(request): 
    return render(request,"hospital/about.html")
    
'''def signup(request):  
    f= Register(request.POST or None)
    if f.is_valid(): 
        data=f.save(commit=False)
        p=f.cleaned_data.get('password')
        data.set_password(p)
        data.save()
        return HttpResponse('Congratulations,user added succesfully')
    return render(request,"hospital/signup.html",{"data":f})'''

'''def appointment(request):
    
    if request.method =="POST":
        ap_name = request.POST.get('ap_name',)
        ap_email= request.POST.get('ap_email')
        ap_phone= request.POST.get('ap_phone')
        ap_desc= request.POST.get('ap_desc')
        img= request.POST.get('img')
        ap_address= request.POST.get('ap_address')
        appointment= Appointment(ap_name=ap_name,ap_email=ap_email,ap_phone=ap_phone,ap_desc=ap_desc,img=img,ap_address=ap_address,ap_date=datetime.today()) 
        appointment.save()
        return HttpResponse("you are succesfully booked your appointment, we will reach to you as soon as posssible")
    return render(request,"hospital/appointment.html")'''

class Appnmnt(LoginRequiredMixin,CreateView):
     login_url="hospital:login"
     model= Appointment
     fields=['dep_name','name','age','email','phone','address','description','previous_prescription','date']
     template_name = 'hospital/appnmnt.html'
     def get_success_url(self):
         pk=self.object.id
         return reverse('hospital:apnmntsuccess',kwargs={'pk':pk})
     
def Bed(request): 
    data=(Beds.objects.all())
    return render(request,"hospital/beds.html",{"data":data})

'''class Signin(View):
    def get(self,request):
        f=Logform(None)
        return render(request,'hospital/login.html',{"data":f})
    def post(self,request):
        f=Logform(request.POST)
        if f.is_valid():
            u=f.cleaned_data.get("username")
            p=f.cleaned_data.get("password")
            ur=authenticate(username=u,password=p)
            nxt=request.GET.get('next')
            print(nxt)
            if ur:
                login(request,ur)
                if nxt:
                    return redirect(nxt)
                else:
                    return redirect('hospital:home')
        return render(request,'hospital/login.html',{"data":f})'''

class AdminLogin(View):
    def get(self, request):
        f=Logform(None)
        k={'data':f}
        return render(request,'hospital/login.html',k)
    def post(self,request):
        f=Logform(request.POST)
        k={'data':f}
        if f.is_valid():
            u=f.cleaned_data.get('username')
            p=f.cleaned_data.get('password')
            ur=authenticate(username=u,password=p) 
            if ur.is_superuser==False:
                 return HttpResponse("you are not admin user!")
            elif ur.is_superuser==True:
                nxt=request.GET.get('next')
                if ur:
                    login(request,ur)
                if nxt:
                    return redirect(nxt)
                else:
                    return redirect('hospital:registeradmin')
        return render(request,'hospital/login.html',k)

class StaffLogin(View):
    def get(self, request):
        f=Logform(None)
        k={'data':f}
        return render(request,'hospital/login.html',k)
    def post(self,request):
        f=Logform(request.POST)
        k={'data':f}
        if f.is_valid():
            u=f.cleaned_data.get('username')
            p=f.cleaned_data.get('password')
            ur=authenticate(username=u,password=p) 
            if ur.is_staff==False:
                return HttpResponse("you cant access this page")
            elif ur.is_staff==True:
                nxt=request.GET.get('next')
            if ur:
                login(request,ur)
                if nxt:
                    return redirect(nxt)
                else:
                     return redirect('hospital:Editapnmnt')
        return render(request,'hospital/login.html',k)

class ActiveLogin(View):
    def get(self, request):
        f=Logform(None)
        k={'data':f}
        return render(request,'hospital/login.html',k)
    def post(self,request):
        f=Logform(request.POST)
        k={'data':f}
        if f.is_valid():
            u=f.cleaned_data.get('username')
            p=f.cleaned_data.get('password')
            ur=authenticate(username=u,password=p)
            nxt=request.GET.get('next')
            if ur:
                login(request,ur)
                if nxt:
                    return redirect(nxt)
                else:
                     return redirect('hospital:home')
        return render(request,'hospital/login.html',k)

class Signup(View): 
    def get(self,request):
        f=Register(None)
        return render(request,'hospital/signup.html',{"data":f})
    def post(self,request):
        f=Register(request.POST)
        if f.is_valid():
            data=f.save(commit=False)
            p=f.cleaned_data.get('password') 
            data.set_password(p)
            data.save()
            return redirect('hospital:login')
        return render(request,'hospital/signup.html',{"data":f})
           
class Signup1(LoginRequiredMixin,View): 
    login_url="hospital:loginadmin"
    def get(self,request):
        f=Register(None)
        return render(request,'hospital/signup.html',{"data":f}) 
    def post(self,request):
        f=Register(request.POST)
        if f.is_valid():
            data=f.save(commit=False)
            p=f.cleaned_data.get('password') 
            data.set_password(p)
            data.is_staff=True
            data.save()
            return redirect('hospital:loginstaff')
        return render(request,'hospital/signup.html',{"data":f})

class Pending_appointments(LoginRequiredMixin,ListView):
    login_url="hospital:loginstaff"
    template_name='hospital/list_appointments.html'
    context_object_name='d'
    def get_queryset(self):
        return (Appointment.objects.filter(date=(date.today())))

def signout(request):
    logout(request)
    return redirect("hospital:home")

class Dtlapview(LoginRequiredMixin,DetailView):
    login_url="hospital:loginstaff"
    model =Appointment
    template_name ="hospital/dtlapview.html"
    context_object_name="data"

class Upapview(LoginRequiredMixin,UpdateView):
    login_url = 'hospital:loginstaff'
    model=Appointment
    fields=['name','age','description','email','phone','address','dep_name','previous_prescription','notes']
    template_name='hospital/upapview.html'
    def get_success_url(self):
         return reverse('hospital:Editapnmnt')
    
class Deleteap(LoginRequiredMixin,DeleteView):
    login_url = 'hospital:staff' 
    model=Appointment 
    success_url=reverse_lazy('hospital:Editapnmnt')
    template_name='hospital/deleteap.html'
    context_object_name='data'

class Apnmntsuccess(LoginRequiredMixin,DetailView): 
    login_url="hospital:login"
    model=Appointment
    template_name='hospital/apnmntsuccess.html'
    context_object_name='data'

def thankyou(request):
    return HttpResponse('<marquee>Thankyou for submitting, We will reach you as soon as possible.</marquee>')

 