from django.shortcuts import render
from . models import Category ,Image,Location


# Create your views here.
def home(request):
  categories =  Category.objects.all()
  locations = Location.objects.all()
  images = Image.objects.all()
 
  
  context = {'categories' :categories,  'locations':locations, 'images':images}
  return render(request, 'home.html' ,context)

def viewPhoto(request,pk):
  images = Image.objects.get(id=pk)
  
  return render(request , 'galley.html' , {'images':images})

def addPhoto(request):
  return render(request, 'add.html')
