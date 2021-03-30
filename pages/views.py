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


url = "https://ashwin-mp.herokuapp.com/about/"
time = datetime.now().time()
if(time.minute>58 and time.minute<60):
    get(url)
    oneob = Count.objects.filter(vis_day = datetime.now().day)[1]
    oneob.delete()

    



def smudge(request):
    return render(request,'pages/smudge.html')


def HomePage(request):
    dt = datetime.now()
    user = request.get_host()
    day = datetime.now().day
    month = datetime.now().month

    #saving every user 
    c = Count()
    c.host = user
    c.vis_day = day
    c.vis_month = month
    c.save()


    #hit recieved
    #months = list(Count.objects.order_by().values_list('vis_day',flat = True).distinct())
    days = list(Count.objects.values_list('vis_day',flat = True).filter(vis_month = month).distinct())
    days.sort()
    fin_counts = []

    for i in days:
        val = Count.objects.filter(vis_day = i).count()
        fin_counts.append(val)

    #fin_counts.reverse()q
    
    context = {'count':fin_counts}
    return render(request, 'pages/home.html',context)

    



class About(TemplateView):
    template_name = 'pages/about.html'

