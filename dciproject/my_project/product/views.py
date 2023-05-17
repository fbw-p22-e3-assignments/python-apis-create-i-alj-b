from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

class ProductFilteredDetailView(DetailView):
    context_object_name = 'product'
    template_name = 'product/product_detail.html'
    # queryset = Product.objects.filter(product_name=self.kwargs['name'])

    def get_queryset(self):
        self.name = self.kwargs['name']
        return Product.objects.filter(product_name=self.name)