from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create, name="meeting_create"),
    path('', views.MeetingListView.as_view(), name="meeting_list"),
    path('<int:pk>/', views.MeetingDetailView.as_view(), name="meeting_view"),
]
