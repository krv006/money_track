from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category,Consumption,Sub_category,Card
# Create your views here.

def index(request):
    
    
    return render(request, 'index_html')


def add_new_consumption(request):
    # post  
    
    return render(request, '')



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
    
    
    
    return render(request, '')
