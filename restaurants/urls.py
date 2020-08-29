from django.urls import path
from .views import HomePageView, DetailView, SearchView


app_name = 'restaurants'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('search/<postcode>/', SearchView.as_view(), name='search'),
    path('search/', HomePageView.as_view(), name="search_home"),
]
