from django.contrib import admin
from .models import Address, Allergy, Category, Cuisine, Food, Restaurant

admin.site.register(Address)
admin.site.register(Allergy)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Food)
admin.site.register(Restaurant)
