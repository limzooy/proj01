from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_news_list_view, name='new_news_list'),
]