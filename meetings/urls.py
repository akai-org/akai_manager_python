from django.urls import path, include
from qr_code import urls as qr_code_urls


from . import views

urlpatterns = [
    path('create/', views.create, name="meeting_create"),
    path('', views.MeetingListView.as_view(), name="meeting_list"),
    path('<int:pk>/', views.MeetingDetailView.as_view(), name="meeting_view"),
    path('activate/<int:pk>/', views.activate, name="meeting_activate"),
    path('edit/<int:pk>/', views.edit, name="meeting_edit"),
    path('register/', views.register, name="meeting_register"),
    path('register/', include(qr_code_urls, namespace='qr_code')),
    path('register/<str:code>/', views.register, name="meeting_register_code"),
    path('delete/<int:pk>', views.MeetingDeleteView.as_view(), name="meeting_delete"),

]
