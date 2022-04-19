from rest_framework import serializers, validators
from users.models import User


class ChangePassordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'full_name', 'address',)

        extra_kwarg = {
            'password': {'write_only': True},
            'email': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(User.objects.all(),f"A user with that email already exists")
                ]
            }
        }
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            address = validated_data['address'],
            full_name = validated_data['full_name'],
        )
        return user