from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name="catalog"),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name="product_detail"),
    path('order/<int:pk>', views.CreateOrder.as_view(), name="product_order"),
]