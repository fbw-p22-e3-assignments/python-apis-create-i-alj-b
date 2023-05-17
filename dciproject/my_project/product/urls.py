from django.urls import path, include 
from .views import ProductListAPIView, ProductRetrieveAPIView, ProductCreateAPIView, ProductDestroyAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='api_list'),
    path('new/', ProductCreateAPIView.as_view(), name='api_create'), 
    path('delete/<product_name>/', ProductDestroyAPIView.as_view(), name='api_delete'), 
    path('detail/<product_name>/', ProductRetrieveAPIView.as_view(), name='api_retrieve'), 
]