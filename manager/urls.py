from django.urls import path
from manager import views

urlpatterns = [
    path('admin_login/', views.LoginAdminView.as_view(), name='admin_login'),
    path('admin_register/', views.AdminRegisterationView.as_view(), name='admin_register'),
    path('admin_profile/', views.AdminProfileView.as_view(), name='admin_profile'),
]