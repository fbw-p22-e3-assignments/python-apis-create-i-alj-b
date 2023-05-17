from django.urls import path, include 
from .views import ProductListView, ProductFilteredListView

urlpatterns = [
    path('', ProductListView.as_view(), name='overview'),
    path('<name>/', ProductFilteredListView.as_view(), name='name_overview'), 
]