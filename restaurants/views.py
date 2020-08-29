from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView
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


class SearchView(TemplateView):
    template_name = 'search.html'

    def post(self, request):
        return redirect('restaurants:search_postcode',
                        postcode=request.POST['postcode_field'])
