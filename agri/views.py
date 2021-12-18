from django.db.models.fields import URLField
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import login, logout, authenticate
import requests
import math
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
            return redirect('login')
        else:
           return redirect('login')
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


def resetPassword(request):
    uname = request.POST['uname']
    password = request.POST['pass']
    newpass = request.POST['pass']
    user = User.objects.filter(username = uname).first()
    if(user.password == password):
        user.set_password(password)
        redirect("/")

def weatherFore(request):
    #if request.method == 'POST':
    #city_name = request.POST['city']
    city_name = "hyderabad"
    app_key = 'd15cab1ad9a0e88a273223c23d953c22'
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={app_key}"
    data_set = requests.get(url).json()
    context = {
            "city_name":data_set["city"]["name"],
            "city_country":data_set["city"]["country"],
            "wind":data_set['list'][0]['wind']['speed'],
            "degree":data_set['list'][0]['wind']['deg'],
            "status":data_set['list'][0]['weather'][0]['description'],
            "cloud":data_set['list'][0]['clouds']['all'],
            "date":data_set['list'][0]["dt_txt"],
            "date1":data_set['list'][1]["dt_txt"],
            "date2":data_set['list'][2]['dt_txt'],
            "date3":data_set['list'][3]['dt_txt'],
            
            "temp":round(data_set["list"][0]["main"]["temp"]-273),
            "temp_min1":math.floor(data_set["list"][1]["main"]["temp_min"]-273),
            "temp_max1":math.ceil(data_set["list"][1]["main"]["temp_max"]-273),
            "temp_min2":math.floor(data_set["list"][2]["main"]["temp_min"]-273),
            "temp_max2":math.ceil(data_set["list"][2]["main"]["temp_max"]-273),
            "temp_min3":math.floor(data_set["list"][3]["main"]["temp_min"]-273),
            "temp_max3":math.ceil(data_set["list"][3]["main"]["temp_max"]-273),
            
            "pressure":data_set["list"][0]["main"]["pressure"],
            "humidity":data_set["list"][0]["main"]["humidity"],
            "sea_level":data_set["list"][0]["main"]["sea_level"],
            
            


        }
    print(context["city_name"])
    return render(request,'agri/weather.html',context)


def maps(request):
    return render(request,"agri/gmaps.html")
