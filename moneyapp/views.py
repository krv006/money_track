from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from .models import Category,Consumption,Sub_category,Card
from .forms import ConsumptionForm
# Create your views here.

def index(request):
    
    
    return render(request, 'index_html')


def add_new_consumption(request):
    if request.method == 'POST':
        form = ConsumptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ConsumptionForm()
    
    context ={
        'form':form,
    }
    return render(request, 'add_new_consumption.html', context)



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
    sub_categoris = Sub_category.objects.all()
    context = {
        'sub_categoris' : sub_categoris
    }
    return render(request, 'sub_category.html' , context)

def sub_category_detail(request , sub_cat_id ):
    sub_category = Sub_category.objects.get(id = sub_cat_id)
    consumptions = Consumption.objects.all()
    context = {
        'sub_category' : sub_category,
        'cosumptions' : consumptions
    }
    return render(request, 'sub_category_detail.html', context )
