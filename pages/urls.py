from os import name
from django.urls import path
from .views import HomePage,About
from . import views

urlpatterns = [
    path('',views.HomePage,name = 'home'),
    path('about/',About.as_view(),name = 'about'),
    
]