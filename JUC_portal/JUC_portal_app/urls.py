from django.urls import path
from . import views

app_name='JUC_potal'

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.newStudent,name='signup'),
    path('login/',views.login,name='login'),
    path('writeBlog/',views.writeBlog,name='login'),


]