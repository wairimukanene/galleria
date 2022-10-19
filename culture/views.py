from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
  return render(request, 'home.html')
def viewPhoto(request,pk):
  return render(request , 'galley.html')
def addPhoto(request):
  return render(request, 'add.html')
