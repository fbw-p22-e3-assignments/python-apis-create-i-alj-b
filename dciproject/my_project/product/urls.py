from django.urls import path, include 
from .views import ProductListAPIView, ProductRetrieveAPIView, ProductCreateAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='api_list'),
    path('new/', ProductCreateAPIView.as_view(), name='api_create'), 
    path('<product_name>/', ProductRetrieveAPIView.as_view(), name='api_retrieve'), 
]