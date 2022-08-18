from django.urls import path
from manager import views

urlpatterns = [
    path('admin_login/', views.LoginAdminView.as_view(), name='admin_login'),
    path('admin_register/', views.AdminRegisterationView.as_view(), name='admin_register'),
    path('admin_profile/', views.AdminProfileView.as_view(), name='admin_profile'),
    path('admin_manager/', views.AdminListView.as_view(), name='admin_manager'),
    path('admin_delete/<int:pk>', views.AdminDeleteView.as_view(), name='admin_delete'),
    path('admin_logout/', views.AdminLogout.as_view(), name='admin_logout'),
    path('admin_sendphone/', views.SendPhone.as_view(), name='admin_sendphone'),
    path('admin_resetpassword/<int:pk>', views.AdminResetPasswordView.as_view(), name='admin_resetpassword'),
    path('admin_changepassword/', views.AdminChangePassword.as_view(), name='admin_changepassword'),
]