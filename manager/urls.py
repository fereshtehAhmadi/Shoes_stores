from django.urls import path
from manager import views

urlpatterns = [
    path('admin_login/', views.LoginAdminView.as_view(), name='admin_login'),
    path('admin_register/', views.AdminRegisterationView.as_view(), name='admin_register'),
    path('admin_profile/', views.AdminProfileView.as_view(), name='admin_profile'),
    path('admin_manager/', views.AdminListView.as_view(), name='admin_manager'),
    path('admin_delete/pk', views.AdminDeleteView.as_view(), name='admin_delete'),
]