from django.urls import path
from accounts import views

urlpatterns = [
    path('send_phone/', views.SendPhoneNumber.as_view(), name='send_phone'),
    path('register/<int:pk>', views.RegisterationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
]