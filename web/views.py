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
        existance = {'message' : 'username already exists'}
        return render(request,"register.html", existance)
    else:
        newUser = User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],email = request.POST['email'],username=request.POST['user'],password=request.POST['passw'])
        return render(request, "register.html")

@csrf_exempt
def login(request):

    return render(request, "login.html")
