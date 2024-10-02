from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar_home'),  # 기본 URL로 캘린더 뷰
    path('<int:year>/<int:month>/', views.calendar_view, name='calendar_month'),  # 연도와 월을 포함한 URL
]