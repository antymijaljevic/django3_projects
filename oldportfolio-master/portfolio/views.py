from django.shortcuts import render
from .models import Project

def home(request):
	projects = Project.objects.all()
	return render(request, 'portfolio/home.html',{'projects':projects})

def projects(request):
	return render(request, 'portfolio/projects.html')

def about(request):
	return render(request, 'portfolio/about.html')