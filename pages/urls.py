from os import name
from django.urls import path
from .views import HomePage,About
from . import views

urlpatterns = [
    path('',HomePage.as_view(),name = 'home'),
    path('about/',About.as_view(),name = 'about'),
    path('graph/',views.Graph,name = 'graph')
]