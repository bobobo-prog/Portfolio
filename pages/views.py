from django.http import request
from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic import TemplateView
from plotly.offline import plot
from plotly.graph_objects import Scatter



def Graph(request):
    x_data = [0,1,2,3,4]
    y_data = [ x**2 for x in x_data ]

    plot_div = plot([Scatter(
        x = x_data,y = y_data,mode = 'lines',name = 'test',opacity = '0.8',marker_color = 'green'
    )],output_type='div')

    return render(request,"Graph.html",context={'plot_div':plot_div})



    



class HomePage(TemplateView):
    template_name = 'pages/home.html'


class About(TemplateView):
    template_name = 'pages/about.html'







    
    