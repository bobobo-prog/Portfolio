from django.urls import path
from .views import HomePage,About

urlpatterns = [
    path('',HomePage.as_view(),name = 'home'),
    path('about/',About.as_view(),name = 'about')
]