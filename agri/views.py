from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'agri/index.html')


def login(request):
    return render(request,"agri/login.html")

def maps(request):
    return render(request,"agri/gmaps.html")