from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
@csrf_exempt


# Create your views here.
def regist(request):
    print("kire khar")
    return render(request,"register.html")


def submit(request):
    print("kir")
    # if User.objects.filter(request.POST['user']).exists():
    #     existance = {'message' : 'username already exists'}
    #     return render(request,"register.html",existance)
    # else :

    newUser = User.objects.create(name=request.POST['name'],username=request.POST['user'],password=request.POST['passw'])
    newUser.save()
    return render(request,"register.html")
