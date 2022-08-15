from django.urls import path
from manager import views

urlpatterns = [
    path('admin_register/', views.AdminRegisterationView.as_view(), name='admin_register'),
]