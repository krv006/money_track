from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [ 
    path('' , index, name='index'),
    path('all_category/', all_category, name='all_category'),
    path('add_new_consumption/', add_new_consumption, name='add_new_consumption'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('sub_category/', sub_category, name='sub_category'),
    path('sub_category_detail/<int:sub_category_id>', sub_category_detail, name='sub_category_detail'),
    path('input/', input, name='input'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),


]
