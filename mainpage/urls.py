from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage_home, name='mainpage_home'),
]