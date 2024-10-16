from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.exhibition_event_list_view, name='exhibition_event_list'),
    # path('admin/', admin.site.urls),
    path('exhibition_event/', views.exhibition_event_list_view),
]
