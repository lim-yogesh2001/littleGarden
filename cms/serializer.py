from rest_framework import serializers
from .models import PrivacyPolicy, AboutUs, ShippingPolicy

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"

class PrivacySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = "__all__"

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingPolicy
        fields = "__all__"