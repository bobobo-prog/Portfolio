from django.http import request
from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic import TemplateView
import requests
import json
from .models import Count
from datetime import date, datetime


def HomePage(request):
    user = request.get_host()
    mon = datetime.now().month
    c = Count()
    c.host = user
    c.vis_month = mon
    c.save()

    n = Count.objects.all().count()
    num_users = [ i for i in range(0,n)]
    num_users = json.dumps(num_users)
    context = {'count':num_users}
    return render(request, 'pages/home.html',context)

    



class About(TemplateView):
    template_name = 'pages/about.html'







    

#     num_vis = request.session.get('num_visits',0)
#     request.session['num_visits'] = num_vis + 1
#     counts = [ i for i in range(0,num_vis)]
#     counts = json.dumps(counts)
#     context = {'hits' : num_vis,'values':counts}    