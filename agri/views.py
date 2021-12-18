from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
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
