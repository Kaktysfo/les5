from django.urls import path, include
from django.contrib import admin
from .views import index
from .import views

urlpatterns = [
    path('', index),
    path('top-sellers/', views.top_sellers_view, name='top-sellers'),  # URL для top-sellers.html
    path('product-detail/<int:product_id>/', views.product_detail_view, name='product-detail'),
]