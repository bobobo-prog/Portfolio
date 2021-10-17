from django.http import request
from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic import TemplateView
import requests
import json
from .models import Count
from datetime import date, datetime
import calendar
from requests import get



    
def smudge(request):
    return render(request,'pages/smudge.html')

    
def blogs(request):
    return render(request,'pages/blogs.html')


def HomePage(request):
    dt = datetime.now()
    user = request.META.get("REMOTE_ADDR")
    day = datetime.now().day
    month = datetime.now().month

    #saving every user 
    c = Count()
    #if(len(Count.objects.all().filter(host = user)<1)):
    c.host = user
    c.vis_day = day
    c.vis_month = month
    c.save()


    #hit recieved
    
    days = list(Count.objects.values_list('vis_day',flat = True).filter(vis_month = month).distinct())
    days.sort()
    fin_counts = []
    
    


    for i in days:
        val = Count.objects.filter(vis_day = i).count()
        fin_counts.append(val//6)

    #fin_counts.reverse()q
    
    context = {'count':fin_counts}
    return render(request, 'pages/home.html',context)

    



class About(TemplateView):
    template_name = 'pages/about.html'

