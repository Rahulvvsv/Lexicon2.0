from django.db.models.fields import URLField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
import requests
import math
import json
from .models import Crop
# import module
from geopy.geocoders import Nominatim

# Create your views here.
def index(request):
    data = Crop.objects.all()
    context = {
    'user':request.user,
    'data' : data
    }
    return render(request,'agri/index.html',context)
def dtail(request,id):
    data = Crop.objects.filter(id = id).first()
    context = {
        'data':data
    }
    return render(request,"agri/cropManagement.html",context)

#login
def loggin(request):
    if request.method == "post":
        uname = request.POST['uname']
        password = request.POST['pwd']
        print(uname)
        user = authenticate(username = uname,password = password)
        if user is not None:
            login(request,user)
            return redirect('login')
        else:
           return redirect('')
    return render(request,"agri/login.html")
#logout
def logingout(request):
    logout(request)
    return redirect('login')

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
            euser.save()
            return redirect('/')
    return render(request,"agri/register.html")



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
    print(context)
    return render(request,'agri/weather.html',context)


def maps(request):
    return render(request,"agri/gmaps.html")


def scrape(request):
    agriculture_url = "https://economictimes.indiatimes.com/news/economy/agriculture"
    data = requests.get(agriculture_url)
    soup = BeautifulSoup(data.content,"html5lib")
    data_div = soup.find("div",attrs={"class":"tabdata"})
    data_div2 = data_div.find_all("div",attrs={"class":"eachStory"})
    array = list()
    for i in data_div2:
        data = i.find("h3")
        data = data.find("a")
        array.append([data.text,data['href']])


    return JsonResponse(array,safe=False)

def scrape_post(request):
    geolocator = Nominatim(user_agent="geoapiExercises")
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        data = data.get("position")
        lat = data["lat"]
        lng = data["lng"]
        location = geolocator.reverse(str(lat)+","+str(lng))
        address = location.raw["address"]
        state = address.get("state","")
        dataa = Crop.objects.all()
        print(dataa)
        array = list()
        for i in dataa:
            print("state",state,"i.states",i.state,type(i.state))
            for j  in i.state:
                print(j)
                if j == state:
                    array.append(j)
        print(state,array)
        return render(request,'agri/gmaps.html',data)
    else:
        return HttpResponse("hiii")
    