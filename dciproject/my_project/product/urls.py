from django.urls import path, include 
from .views import ProductListAPIView, ProductRetrieveAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='api_list'),
    path('<product_name>/', ProductRetrieveAPIView.as_view(), name='api_retrieve'), 
]