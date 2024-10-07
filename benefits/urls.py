from django.urls import path
from . import views

urlpatterns = [
    path('', views.benefit_list_view, name='benefits_list'),
]
