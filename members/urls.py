from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="member_list"),
    path('<int:pk>/', views.DetailView.as_view(), name="member_detail"),
    path('<int:pk>/delete', views.DeleteView.as_view(), name="member_delete"),
]
