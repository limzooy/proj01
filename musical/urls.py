from django.urls import path
from . import views

urlpatterns = [
    path('', views.musical_list_view, name='musical_list'), 
]