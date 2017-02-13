from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^register/', views.regist),
    url(r'^data/', views.submit),
    url(r'^login/', views.login),
    url(r'', views.regist),

]