from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User,File
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def regist(request):
    return render(request, "register.html")


@csrf_exempt
def submit(request):
    if User.objects.filter(username=request.POST['user']).exists():
        context = {'error': 'true', 'message' : 'username already exists!'}
        return render(request, "register.html", context)
    else:
        User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],email = request.POST['email'],username=request.POST['user'],password=request.POST['passw'])
        context = {'error': 'false', 'message': 'user created'}
        return render(request, "register.html", context)


@csrf_exempt
def login(request):
    if User.objects.filter(username=request.POST['user']).exists():
        newUser = User.objects.filter(username=request.POST['user']).get()
        if request.POST['passw'] == newUser.password:
            return render(request, "welcome.html")

    data = {'message': 'wrong username or password!'}
    return render(request, "login.html", data)


def showLogin(request):
    return render(request, "login.html")


def upload(request):
    File.objects.create(file=request.FILES.get('myFile'), user=User.objects.filter(username='adelante').get())
    return render(request, "welcome.html")