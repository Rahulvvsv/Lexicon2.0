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

def maps(request):
    return render(request,"agri/gmaps.html")
