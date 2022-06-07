from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from .models import Orders
from .serializer import OrderSerailizer


class UserOrdersView(APIView):

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            orders = Orders.objects.filter(user_id=user)
            serializer = OrderSerailizer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)


class OrdersView(APIView):

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            orders = Orders.objects.filter(user_id=user_id)
            serializer = OrderSerailizer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer = OrderSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    def get(self, request, id):
        try:
            orders = Orders.objects.get(id=id)
            serializer = OrderSerailizer(orders)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response("Not Found", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        orders = Orders.objects.get(id=id)
        serializer = OrderSerailizer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        orders = Orders.objects.get(id=id)
        orders.delete()
        return Response("Deleted Successfully", status=status.HTTP_404_NOT_FOUND)
