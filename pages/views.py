from django.http import request
from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic import TemplateView


def Graph(request):
       return render(request, 'pages/Graph.html')


class HomePage(TemplateView):
    template_name = 'pages/home.html'


class About(TemplateView):
    template_name = 'pages/about.html'







    
    