# portfolio/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),       
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('res/', views.download_resume, name='download_resume'), 
]