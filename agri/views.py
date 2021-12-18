from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'agri/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pass']
        
    return render(request,"agri/login.html")