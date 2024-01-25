from django.shortcuts import render
from .models import Category,Consumption,Sub_category,Card
# Create your views here.

def index(request):
    
    
    return render(request, 'index_html')


def add_new_consumption(request):
    # post  
    
    return render(request, '')


def all_category(request):
    categorys = Category.objects.all()
    context = {
        'categorys' : categorys
    }
    
    return render(request, 'all_category.html' , context)


def category_detail(request , Sub_category):
    category = Category.objects.filter( id = Sub_category)
    #sub category ni ozi id ga
    context = {
        'category' : category
    }
    
    
    return render(request,'category_detail.html' , context)



def sub_category(request):
    
    
    
    return render(request, '')