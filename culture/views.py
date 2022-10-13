from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
  return render(request, 'home.html')
def tribe(request,pk):
  return render(request , 'galley.html')
