from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list_view, name='board'),
]