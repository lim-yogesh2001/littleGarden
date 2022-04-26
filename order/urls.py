from django import views
from django.urls import path
from .views import UserOrdersView, OrdersView, OrderDetailView

urlpatterns = [
    path('user-orders/<int:user_id>', UserOrdersView.as_view(), name='user-orders'),
    path('orders-list/<int:user_id>', OrdersView.as_view(), name="orders-list"),
    path('order-details/<int:id>', OrderDetailView.as_view(), name='order-detail')
]
