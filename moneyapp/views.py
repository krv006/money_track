from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category,Consumption,Sub_category,Card
# Create your views here.

def index(request):
    
    
    return render(request, 'index_html')


def add_new_consumption(request):
    name = Consumption.objects.filter()
    info = Consumption.objects.all()
    cost = Consumption.objects.all()
    sub_category = Consumption.objects.all()
    time = Consumption.objects.all()
    status = Consumption.objects.all()
    context = {
        'name' : name ,
        'info' : info ,
        'cost' : cost ,
        'sub_xategory' : sub_category ,      
        'time' : time ,
        'status' : status , 
    }   
    
    return render(request, 'add_new_consumption', context)



def all_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'all_category.html', context)

def category_detail(request, sub_category_id):
    category = Category.objects.all()
    context = {
        'category': category,
        'sub_category_id': sub_category_id,
    }
    return render(request, 'category_detail.html', context)


def sub_category(request):
    name = Sub_category.objects.all()
    context = {
        'name' : name
    }
    return render(request, 'sub_category.html' , context)
