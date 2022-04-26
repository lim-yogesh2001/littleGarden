from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Categories, Product, ProductReview
from .serializer import CategorySerializer, ProductSerialzier, ProductReviewSerializer



# Category API View
class CategoryView(APIView):
    def get(self, request):
        try:
            categories = Categories.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Categories.DoesNotExist:
            return Response({"Category Not Found"}, status=status.HTTP_404_NOT_FOUND)

class CategoryProductView(APIView):
     def get(self, request, category_id):
        try:
            categories = Categories.objects.get(id=category_id)
            products = Product.objects.filter(category_id=categories)
            serializer = ProductSerialzier(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Categories.DoesNotExist:
            return Response({"Products Not Found"}, status=status.HTTP_404_NOT_FOUND)

# Category API View


# Product API View
class RecentlyAddedProducts(APIView):
    def get(self, request):
        try:
            products = Product.objects.filter(is_recently_added=True)
            serializer = ProductSerialzier(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"Products Not Found"}, status=status.HTTP_404_NOT_FOUND)


class PopularProducts(APIView):
    def get(self, request):
        try:
            products = Product.objects.filter(is_popular=True)
            serializer = ProductSerialzier(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"Products Not Found"}, status=status.HTTP_404_NOT_FOUND)

class ProductsView(APIView):
    def get(self, request):
        try:
            products = Product.objects.filter(is_popular=False, is_recently_added=False)
            serializer = ProductSerialzier(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"Products Not Found"}, status=status.HTTP_404_NOT_FOUND)

class ProductDetail(APIView):
    def get(self, request, id):
        try:
            products = Product.objects.get(id=id)
            serializer = ProductSerialzier(products)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"Products Not Found"}, status=status.HTTP_404_NOT_FOUND)

# Product API View


# Product Review API
class ProductReviews(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            reviews = ProductReview.objects.filter(product_id=product)
            serializer = ProductReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProductReview.DoesNotExist():
            return Response({"Error":"Product Reviews Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Something Went Wrong!!!!!")



        
class ProductReviewDetail(APIView):
    def get(self, request, id):
        try:
            review = ProductReview.objects.get(id=id)
            serializer = ProductReviewSerializer(review)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProductReview.DoesNotExist:
            return Response("Review Not Found")
    
    def put(self, request, id):
        try:
            review = ProductReview.objects.get(id=id)
            serializer = ProductReviewSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Something Went Wrong!!!")
        
    def delete(self, request, id):
        review = ProductReview.objects.get(id=id)
        review.delete()
        return Response("Deleted Successfully!!!", status=status.HTTP_404_NOT_FOUND)           
# Product Review API
