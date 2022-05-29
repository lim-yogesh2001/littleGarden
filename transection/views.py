from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PaymentSerializer, TransectionSerializer
from transection.models import Payment, Transection
from users.models import User


# Create your views here.
class PaymentView(APIView):

    def get(self, request):
        try:
            payment_method = Payment.objects.all()
            serializer = PaymentSerializer(payment_method, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)

class TransectionView(APIView):
    
    def get(self, request):
        try:
            transections = Transection.objects.all()
            serializer = TransectionSerializer(transections, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Transection.DoesNotExist:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        serializer = TransectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserTransectionView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            transections = Transection.objects.filter(user_id=user)
            serializer = TransectionSerializer(transections, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"Not Found"}, status=status.HTTP_404_NOT_FOUND)
            

class TransectionDetailView(APIView):
    def get(self, request, id):
        try:
            transection = Transection.objects.get(id=id)
            serializer = TransectionSerializer(transection)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Transection.DoesNotExist:
            return Response({"Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        transection = Transection.objects.get(id=id)
        serializer = TransectionSerializer(transection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



