from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^register/', views.regist),
    url(r'^data/', views.submit),
    url(r'^usercheck/', views.login),
    url(r'^login/', views.showLogin),
    url(r'', views.regist),

]