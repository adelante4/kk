from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def regist(request):
    return render(request, "register.html")

@csrf_exempt
def submit(request):
    if User.objects.filter(username=request.POST['user']).exists():
        return render(request, "register.html")
    else:
        newUser = User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],email = request.POST['email'],username=request.POST['user'],password=request.POST['passw'])
        return render(request, "register.html")

@csrf_exempt
def login(request):
    if User.objects.filter(username=request.POST['user']).exists():
        newUser = User.objects.filter(username=request.POST['user']).get()
        if request.POST['passw'] == newUser.password:
            return render(request, "welcome.html")
    else:
        return render(request,"login.html")

def showLogin(request):
    return render(request, "login.html")