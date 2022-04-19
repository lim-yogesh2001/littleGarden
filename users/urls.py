from django.urls import path, include
from . import views
from knox import views as knox_views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-the-password'),
    path('password-reset/', include('django_rest_passwordreset.urls'), name='reset-password')
]
