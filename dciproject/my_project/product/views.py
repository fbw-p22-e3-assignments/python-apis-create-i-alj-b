from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

class ProductFilteredListView(ListView):
    context_object_name = 'products'
    template_name = 'product/product_name_list.html'
    # queryset = Product.objects.filter(product_name=self.kwargs['name'])

    def get_queryset(self):
        self.name = self.kwargs['name']
        return Product.objects.filter(product_name=self.name)