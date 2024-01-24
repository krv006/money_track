from django.shortcuts import render
from .models import Category,Consumption,Sub_category,Card
# Create your views here.

def index(request):
    
    
    return render(request, 'index_html')


def add_new_consumption(request):
    # post  
    
    return render(request, '')


def all_category(request):
    
    
    
    return render(request, '')


def category_detail(request):
    
    
    
    return render(request,'')



def sub_category(request):
    
    
    
    return render(request, '')