from django.urls import path
from manager import views

urlpatterns = [
    path('admin_login/', views.LoginAdminView.as_view(), name='admin_login'),
    path('admin_register/', views.AdminRegisterationView.as_view(), name='admin_register'),
    path('admin_manager/<int:pk>', views.ManagerInformationView.as_view(), name='admin_manager'),
    
    path('admin_profile/', views.AdminShowProfileView.as_view(), name='admin_profile'),
    path('admin_edit/', views.AdminEditView.as_view(), name='admin_edit'),
    path('admin_edit_manager/', views.AdminManagerEditView.as_view(), name='admin_edit_manager'),
    
    path('admin_manager/', views.AdminListView.as_view(), name='admin_manager'),
    path('admin_delete/<int:pk>', views.AdminDeleteView.as_view(), name='admin_delete'),
    path('admin_logout/', views.AdminLogout.as_view(), name='admin_logout'),
    path('admin_sendphone/', views.SendPhone.as_view(), name='admin_sendphone'),
    path('admin_resetpassword/<int:pk>', views.AdminResetPasswordView.as_view(), name='admin_resetpassword'),
    path('admin_changepassword/', views.AdminChangePassword.as_view(), name='admin_changepassword'),
]