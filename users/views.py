from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from .serializer import RegisterSerializer, ChangePassordSerializer
from .models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializer import UserSerializer
from knox.auth import AuthToken
from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail
# Create your views here.



@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    _, token = AuthToken.objects.create(user)
    return Response({
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'password': user.password,
            'address': user.address,
            'full_name': user.full_name,
        },'token': token}, 
        status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)
    return Response({
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        },'token': token}, 
    status=status.HTTP_200_OK)


class ChangePasswordView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePassordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old password": "Wrong"}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Your Password Updated'
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@receiver(reset_password_token_created)
def password_reset_token(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(
        reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        "Password Reset for {title}".format(title="Hamro Cinema"),
        email_plaintext_message,
        'boss@gmail.com',
        [reset_password_token.user.email]
    )

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def profile_view(request, id):
    if request.method == 'GET':
        profile = User.objects.get(id=id)
        serializer = UserSerializer(profile, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        profile = User.objects.get(id=id)
        serializer = UserSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_notification()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

