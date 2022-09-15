from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("ddos/", views.nmap, name="ddos"),
    path("ip/", views.ip, name="ip"),
    #path("ping/", views.ping, name="ping"),

]   