from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [ 
    path('', index , ),
    path('' , all_category , ),
    path('' , add_new_consumption, ),
    path('' , category_detail ,  ),
    path('' , sub_category , ),

]