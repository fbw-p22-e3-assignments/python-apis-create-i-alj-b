from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]

# Create your views here.

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'product_name'
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    lookup_field = 'product_name'
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]