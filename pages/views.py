from django.http import request
from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic import TemplateView
import requests
from requests import status_codes
import json



def HomePage(request):
    num_vis = request.session.get('num_visits',0)
    request.session['num_visits'] = num_vis + 1
    counts = [ i for i in range(0,num_vis)]
    counts = json.dumps(counts)
    context = {'hits' : num_vis,'values':counts}
    
    return render(request, 'pages/home.html',context)

    



class About(TemplateView):
    template_name = 'pages/about.html'







    
    