from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def index(request):
    return render(request,'agri/index.html')

#login
def login(request):
    if request.method == "POST":
        uname = request.POST['uname']
        password = request.POST['pwd']
        user = authenticate(username = uname,password = password)
        if user is not None:
            login(request,user)
            return redirect('landingpage')
        else:
           return redirect('landingpage')
    return render(request,"agri/login.html")
#logout
def logout(request):
    logout(request)
    return redirect('landingpage')

#Registration
def resitration(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        password = request.POST['password']
        user = User(username = username,first_name = first_name,last_name = last_name)
        user.set_password(password)
        user.save()
        utype = request.POST['type']
        if utype == 'farmer':
            adhaar = request.POST['adhaar']
            village = request.POST['village']
            district = request.POST['district']
            state = request.POST['state']
            auser = AgriUser(user = user,adhaar = adhaar,village = village,district = district,state = state)
            auser.save()
            return redirect('/')
        if utype == 'govt':
            EmpId = request.POST["empId"]
            address = request.POST['address']
            euser = GovempUser(user = user,EmployeeId = EmpId,Address = address)
            return redirect('/')
    return render(request,"agri/register.html")




def maps(request):
    return render(request,"agri/gmaps.html")
