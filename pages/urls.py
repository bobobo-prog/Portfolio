from os import name
from django.urls import path
from .views import HomePage,About
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.HomePage,name = 'home'),
    path('about/',About.as_view(),name = 'about'),
    path('smudgelord/',views.smudge,name = 'smudge'),
    path('blogs/',views.blogs,name = 'blogs')
    
]
