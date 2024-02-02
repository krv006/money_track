from django.contrib import admin
from .models import Sub_category
from .models import Card
from .models import Consumption
from .models import Category
# from .models import Plastic_card

# Register your models here.

admin.site.register(Sub_category)
admin.site.register(Card)
admin.site.register(Consumption)
admin.site.register(Category)
# admin.site.register(Plastic_card)