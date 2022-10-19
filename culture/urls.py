from django.urls import path 
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    path('galley/<str:pk>/', views.viewPhoto,name='galley'),
    path('add/',views.addPhoto,name='add'),
    
    
  
]
