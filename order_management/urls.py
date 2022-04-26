from django.urls import  path
from .views import *
urlpatterns = [
    path('',AdminOrderView,name='ord-view'),
    path('ord-update/<int:pk>/',AdminOrderUpdate,name='ord-update'),
    path('ord-cancel/<int:pk>/',AdminOrderCancel,name='ord-cancel'),
    
]
