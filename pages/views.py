from django.http import request
from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic import TemplateView
import requests
import json
from .models import Count
from datetime import date, datetime



def smudge(request):
    return render(request,'pages/smudge.html')


def HomePage(request):
    user = request.get_host()
    day = datetime.now().day
    c = Count()
    c.host = user
    c.vis_month = day
    c.save()
    #--------hit recieved-------------

    months = list(Count.objects.order_by().values_list('vis_month',flat = True).distinct())

    fin_counts = []

    for i in months:
        val = Count.objects.filter(vis_month = i).count()
        fin_counts.append(val)

    #fin_counts.reverse()
    
    context = {'count':fin_counts}
    return render(request, 'pages/home.html',context)

    



class About(TemplateView):
    template_name = 'pages/about.html'







    

#     num_vis = request.session.get('num_visits',0)
#     request.session['num_visits'] = num_vis + 1
#     counts = [ i for i in range(0,num_vis)]
#     counts = json.dumps(counts)
#     context = {'hits' : num_vis,'values':counts}    




# n = Count.objects.all().count()
# num_users = [ i for i in range(0,n)]
# num_users = json.dumps(num_users)