from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('', views.home, name='home'),
    path('addResume/', views.addResume, name='add-resume'),
    path('about/', views.about, name='about'),

]
