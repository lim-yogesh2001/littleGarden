from django.urls import path

from .views import PaymentView, TransectionView, TransectionDetailView

urlpatterns = [
    path('payments/', PaymentView.as_view(), name='payment-method-list'),
    path('transections/', TransectionView.as_view(), name='transection-list'),
    path('transection-detail/<int:id>', TransectionDetailView.as_view(), name='transection-detail'),
]
