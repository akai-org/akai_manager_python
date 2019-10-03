"""akai_manager_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from meetings import views as meeting_views
from members import views as member_views
from django.contrib.auth.views import auth_logout
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('meetings/create', meeting_views.create, name="meeting_create"),
    path('meetings/<int:pk>/', meeting_views.MeetingDetailView.as_view(), name="meeting_view"),
    path('', member_views.login, name="login"),
    path('', include('social_django.urls', namespace="social")),
    path('logout/', auth_logout, {'next_page': settings.LOGOUT_REDIRECT_URI}, name='logout'),
]
