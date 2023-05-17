from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]

# Create your views here.

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveAPIView(RetrieveAPIView):
    # context_object_name = 'product'
    # template_name = 'product/product_detail.html'
    # queryset = Product.objects.filter(product_name=self.kwargs['name'])
    queryset = Product.objects.all()
    lookup_field = 'product_name'
    serializer_class = ProductSerializer

    # def get_queryset(self):
    #     self.name = self.kwargs['name']
    #     return Product.objects.filter(product_name=self.name)