from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view()),
    path('privacy/', views.PrivacyView.as_view()),
    path('shipping/', views.ShippingView.as_view())
]
