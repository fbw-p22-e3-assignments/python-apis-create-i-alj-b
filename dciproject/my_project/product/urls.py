from django.urls import path, include 
from .views import ProductListAPIView, ProductRetrieveAPIView, ProductCreateAPIView, ProductDestroyAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='api_list'),
    path('new/', ProductCreateAPIView.as_view(), name='api_create'), 
    path('delete/<product_name>/', ProductDestroyAPIView.as_view(), name='api_delete'), 
    path('detail/<product_name>/', ProductRetrieveAPIView.as_view(), name='api_retrieve'), 
    path('api-auth-token/', obtain_auth_token, name='api-auth-token'),
]

# Requires post request to be sent to api-auth-token with following json body:

# {
#   "username": 
#     "name"
#   ,
#   "password": 
#     "password"
# }


# Add HTTP Authorization header with the following contents::

# Token <token>