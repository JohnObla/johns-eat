from django.views.generic import ListView, DetailView
from .models import Food, Restaurant


class HomePageView(ListView):
    model = Restaurant
    context_object_name = 'restaurants_list'
    template_name = 'home.html'


class DetailView(DetailView):
    model = Restaurant
    template_name = 'restaurants_detail.html'


class FoodListView(ListView):
    model = Food
    context_object_name = 'food_list'
    template_name = 'food_list.html'
