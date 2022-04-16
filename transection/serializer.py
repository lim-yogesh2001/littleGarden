from rest_framework import serializers
from .models import Payment, Transection

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields="__all__"

class TransectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transection
        fields="__all__"