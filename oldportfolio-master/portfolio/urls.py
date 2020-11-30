from . import views
from django.urls import path

app_name = 'portfolio'

urlpatterns = [
    path('projects/', views.projects, name ='projects'),
    path('about/', views.about, name ='about'),
]