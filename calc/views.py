from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from .models import Destination_from

# Create your views here.
# class CalcView(ListView):
#     model = Destination_from
#     template_name = 'calc.html'

def index(request):
    return  HttpResponse({'tt':'Freightlitica Calculator'})

def destionation_from(request):
    return render(request,'calc/destination_from')