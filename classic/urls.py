from django.urls import path
from . import views

urlpatterns = [
    path('', views.classic_list, name='classic_list'),
]
