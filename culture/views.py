from django.shortcuts import render
from . models import Category ,Image,Location


# Create your views here.
def home(request):
  categories =  Category.objects.all()
  locations = Location.objects.all()
  context = {'categories' :categories,  'locations':locations}
  return render(request, 'home.html' ,context)
def viewPhoto(request,pk):
  return render(request , 'galley.html')
def addPhoto(request):
  return render(request, 'add.html')
