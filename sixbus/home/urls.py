from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="index"),
    path("/add1", views.add_bus1, name="add"),
    path("/add2", views.add_bus2, name="add2"),
    path("/asd", views.v, name="v"),



]