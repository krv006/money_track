from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from .models import Category,Consumption,Sub_category,Card
from .forms import ConsumptionForm
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate

# Create your views here.

def index(request):
    name = Category.objects.all()
    context = {
        'name' : name
    }
    
    return render(request, 'index.html',context)


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

def category_detail(request, category_id):
    category = Category.objects.all()
    context = {
        'category': category,
        'category_id': category_id,
    }
    return render(request, 'category_detail.html', context)


def sub_category(request):
    sub_categoris = Sub_category.objects.all()
    context = {
        'sub_categoris' : sub_categoris
    }
    return render(request, 'sub_category.html' , context)



def sub_category_detail(request, sub_category_id):
    sub_category = Sub_category.objects.get(id=sub_category_id)
    consumption = Consumption.objects.filter(sub_category=sub_category)
    total_cost = Consumption.objects.filter(sub_category=sub_category_id).aggregate(Sum('cost'))['cost__sum'] or 0

    context = {
        'sub_category': sub_category,
        'consumption': consumption,
        'total_cost': total_cost,
    }

    return render(request, 'sub_category_detail.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index') 
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})