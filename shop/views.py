from django.views.generic import TemplateView, ListView
from .models import Food


class HomePageView(TemplateView):
    template_name = 'home.html'


class FoodListView(ListView):
    model = Food
    context_object_name = 'food_list'
    template_name = 'food_list.html'
