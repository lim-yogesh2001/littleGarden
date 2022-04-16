from django.urls import path

from .views import PaymentView, TransectionView, UserTransectionView, TransectionDetailView

urlpatterns = [
    path('payments/', PaymentView.as_view(), name='payment-method-list'),
    path('transections/', TransectionView.as_view(), name='transection-list'),
    path('transection-detail/<int:id>', TransectionDetailView.as_view(), name='transection-detail'),
    path('user-transections/<int:user_id>', UserTransectionView.as_view(), name='user-transections'),
]
