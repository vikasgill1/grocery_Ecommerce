from django.urls import  path
from .views import *
urlpatterns = [
    path('',AdminProductView,name='prod-view'),
    path('prod-add/',AdminProductAdd.as_view(),name='prod-add'),
    path('prod-update/<int:pk>/',AdminProductUpdate.as_view(),name='prod-update'),
    path('prod-delete/<int:pk>/',AdminProductdelete,name='prod-delete'),
]
