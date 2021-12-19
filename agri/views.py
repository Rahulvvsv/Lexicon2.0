from os import stat
from django.db.models.fields import URLField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse,HttpResponseRedirect
from django.urls import reverse
import requests
from bs4 import BeautifulSoup
import requests
import math
import json
from .models import Crop
from django.contrib.auth.decorators import login_required
# import module
from geopy.geocoders import Nominatim
from .models import *
from .forms import *



def landing(request):
    objects = PublishUser.objects.order_by('-id')
    context ={'lists':objects}
    return render(request,'agri/landing.html',context)
# Create your views here.
def index(request):
    data = Crop.objects.all()
    user=request.user
    if user.is_authenticated:
        auser = AgriUser.objects.filter(user=user).first()
        context = {
        'auser' : auser,
        'user' : user,
        'data' : data
        }
    else:
        context = {
       
        'data' : data
        }
    return render(request,'agri/home.html',context)
def dtail(request,id):
    data = Crop.objects.filter(id = id).first()
    context = {
        'data':data
    }
    return render(request,"agri/cropManagement.html",context)

#login
def user_login(request):
    print("hello")
    if request.method == "POST":
        print("hellllllll")
        uname = request.POST['uname']
        password = request.POST['pwd']
        
        print(uname)
        print(password)
        user = authenticate(request,username = uname,password = password)
        if user:

            if user.is_active:
                login(request,user)
                print("login succussful")
                return redirect('home')
            else:
                return HttpResponse("somethin went wrong")
        else:
            print("someone tried to login and failed ")
            print(f"Username :{username} and password :{password}")
            return HttpResponse("Invalid login credentials")
    else:
        return render(request,"agri/login.html")
#logout
def logingout(request):
    logout(request)
    return redirect('home')




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
    return JsonResponse(json.dumps(context),safe=False)


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

data_dict = {"Telangana":'TS',"Tamil Nadu":"TN","Karnataka":"KA"}
state1 = "Karnataka"

def scrape_post(request):
    geolocator = Nominatim(user_agent="geoapiExercises")
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        data = data.get("position")
        lat = data["lat"]
        lng = data["lng"]
        location = geolocator.reverse(str(lat)+","+str(lng))
        address = location.raw["address"]
        global state1
        state1 = address.get("state","")
 
        
        
        return render(request,"agri/gmaps.html")
    else:
        return HttpResponse("hiii")
    
def cropss(request):

    dataa = Crop.objects.all()
    print(dataa)
    array = list()
    for i in dataa:
        print("state",state1,"i.states",i.state,type(i.state))
        for j  in i.state:
            print(j)
            if state1 == j:
                array.append(j)
                array.append(i.name)
                array.append(i.fertilizers)
                array.append(i.pesticides)
    print(array)
    return JsonResponse(array,safe=False)


def registration(request):
    if request.method == "POST":
        print("inside post")
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        password = request.POST['password']
        rpassword = request.POST['rpassword']
        print(first_name)
        user = User(username = username,first_name = first_name,last_name = last_name)
        if password == rpassword:
            user.set_password(password)
            user.save()
        else:
            return redirect('uregister')
        phone = request.POST['phone']
        auser = AgriUser(user = auser,phone =phone,is_farmer = True )
        auser.save()
   
        adhaar = request.POST['adhaar']
        village = request.POST['village']
        district = request.POST['district']
        state = request.POST['state']
        fuser = FarmerUser(user = auser,adhaar = adhaar,village = village,district = district,state = state)
        fuser.save()
        return redirect('login')
       
    return render(request,"agri/register.html")

def eregistration(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        password = request.POST['password']
        rpassword = request.POST['rpassword']
        user = User(username = username,first_name = first_name,last_name = last_name)
        if password == rpassword:
            user.set_password(password)
            user.save()
        else:
            return redirect('register')
        phone = request.POST['phone']
        auser = AgriUser(user = user,phone =phone,is_Employee = True )
        auser.save()
    

        EmpId = request.POST["empId"]
        address = request.POST['address']
        euser = GovempUser(user = auser,EmployeeId = EmpId,Address = address)
        euser.save()
        return redirect('login')
    return render(request,"agri/eregister.html")

    
def dtail(request,id):
    data = Crop.objects.filter(id = id).first()
    context = {
        'data':data
    }
    return render(request,"agri/cropManagement.html",context)


@login_required
def postmaker(request):

    pk = request.user.id
    model = User.objects.get(id=pk)
    model1 = model.stories.order_by('-id')
    print(model)
    context = {'objects':model1}

    return render(request,'agri/blogs.html',context)

@login_required
def newposter(request):
    if request.method == "POST":
        
        form = BlogContent1Form(request.POST)
        print('hello1')
        if form.is_valid():
            print('hello2')

            # form.user=user
            # form.save()
            user1= request.user

            user = User.objects.get(id=user1.id)
            # user = request.user.userna
            title = form.cleaned_data['title']
            story = form.cleaned_data['story']


            print('hello3')

            form11 = BlogContent11(user=user,title=title,story=story)

            print('hello4')
            form11.save()
            print('hello5')
            return HttpResponseRedirect(reverse('landing'))
        else:
            print(form.errors)
    return render(request,'agri/newpost.html')

def publish(request,pk):
    content = BlogContent11.objects.get(id=pk)

    print('hello')
    if request.method == "POST":
        print('hello')
        author = request.POST['user']
        title = request.POST['title']
        story = request.POST['story']
        model = PublishUser(author=author,title=title,story=story)
        model.save()
        content = BlogContent11.objects.get(id=pk)
        content.publish = True
        content.save()


        return HttpResponseRedirect(reverse('landing'))


def comments(request,pk):
    if request.method == 'POST':
        form = CommentForms( request.POST)
        if form.is_valid():

            content = form.cleaned_data['comment']

            user = PublishUser.objects.get(id=pk)

            model = CommentUser(post=user,comment=content)
            model.save()

            return HttpResponseRedirect(reverse('landing'))
        else:
            print(form.errors)
            return HttpResponse("Comment Failed1")

    else:
        return HttpResponse("Comment Failed")



@login_required(login_url = 'login')
def addcrop(request):
    

    if request.method == "POST":
            cropname = request.POST['cropname']
            season = request.POST['season']
            crop_info = request.POST['crop_info']
            climate = request.POST['climate']
            states = request.POST['states']
            price = request.POST['price']
            photo = request.POST['photo']
            pesticides = request.POST['pest']
            fertilizers =request.POST['fert']
            seed = request.POST['seed']
            soil_health = request.POST['sh']
            soil_info = request.POST['si']
            crop = Crop(name = cropname,crop_info = crop_info,season = season,climate = climate,state = states,price = price,
                photo = photo,pesticides = pesticides,fertilizers = fertilizers,seed  = seed,soil_health = soil_health,soil_info = soil_info )
            crop.save()

            return redirect('/')
    
    return render(request, "agri/addcrop.html")



def tpa(request,id):
    crop = Crop.objects.filter(id = id).first()
    train = Training.objects.filter(crop = crop).first()
    context = {
    'train':train,
    
    }
    return render(request,"agri/tpa.html",context)