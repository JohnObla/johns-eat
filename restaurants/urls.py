from django.urls import path
from .views import HomePageView, FoodListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('food/', FoodListView.as_view(), name='food'),
]
