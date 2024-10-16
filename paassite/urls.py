"""
URL configuration for paassite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from .views import *

from django.urls import path, include
from mainpage import views as main_views  # mainpage의 뷰를 임포트

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.mainpage_home, name='home'),  # 루트 URL을 홈 뷰로 설정
    path('polls/', include('polls.urls')),
    path('mainpage/', include('mainpage.urls')),
    path('search/', include('search.urls')),
    path('login/', include('login.urls')),
    path('calendar_site/', include('calendar_site.urls')),
    path('classic/', include('classic.urls')),
    path('musical/', include('musical.urls')),
    path('play/', include('play.urls')),
    path('exhibition_event/', include('exhibition_event.urls')),
    path('board/', include('board.urls')),
    path('new_news/', include('new_news.urls')),
]