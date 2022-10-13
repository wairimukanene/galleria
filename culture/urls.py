from django.urls import path 
from . import views



urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('tribe/<str:pk>/', views.tribe,name='tribe'),
    
    
  
]
