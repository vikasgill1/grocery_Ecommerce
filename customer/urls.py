from django.urls import path
from customer.views import *
urlpatterns = [
 
    path('',Product_view.as_view(),name='home'),
    path('product-detail/<int:pk>/',Product_detail.as_view(),name='product-detail'),
    path('Product_Cate_detail/<int:pk>/',Product_Cate_detail.as_view(),name='category-detail'),
    path('AddToCart/<int:pk>/',Add_to_cart, name='add-to-cart'),
    path('cartView/',CartView,name='cartView'),
    path('pluscart/<int:pk>/',plus_quantity,name='minuscart'),
    path('minuscart/<int:pk>/',minus_quantity,name='pluscart'),
    path('orders/', orders, name='orders'),
    path('checkout/', checkout, name='checkout'),
    path('order_placed/',orderPlace,name='order-place'),
    path('orders/', orders, name='orders'),
]