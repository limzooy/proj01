from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_home, name='search_home'),
    path('results/', views.search_results, name='search_results'),
]