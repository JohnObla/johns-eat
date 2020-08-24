from django.urls import path
from .views import HomePageView, FoodListView, DetailView


app_name = 'restaurants'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
]
