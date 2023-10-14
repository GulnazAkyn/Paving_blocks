from django.urls import path
from . import views

urlpatterns = [
    path('product-list/', views.ProductListAPIView.as_view()),
    path('product-list/<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('image-list/', views.ImageListAPIView.as_view()),
]
