from django.urls import path
from . import views

urlpatterns = [
    path('', views.play_list_view, name='play_list'), 
]