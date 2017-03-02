from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
    url(r'^register/', views.regist),
    url(r'^data/', views.submit),
    url(r'^usercheck/', views.login),
    url(r'^login/', views.showLogin),
    url(r'^upload/', views.upload),
    url(r'', views.regist),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)