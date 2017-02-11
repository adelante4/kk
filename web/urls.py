from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^register/', views.regist),
    url(r'^data/', views.submit),
    url(r'^menu/', views.menu),
]