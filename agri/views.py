from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'agri/index.html')


def login(request):
<<<<<<< HEAD
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pass']
        
    return render(request,"agri/login.html")
=======
    return render(request,"agri/login.html")

def maps(request):
    return render(request,"agri/gmaps.html")
>>>>>>> 0b5a94eea46549a41a36552c697e847933852c6a
