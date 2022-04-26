from django.urls import  path,include
from .views import Category_Upadate, Category_add, CategoryView, Categorydelete

urlpatterns = [
    path('', CategoryView,name='cate-view'),
    path('categ-add/',Category_add.as_view(),name='categ-add'),
    path('categ-update/<int:pk>/',Category_Upadate.as_view(),name='categ-update'),
    path('categ-delete/<int:pk>/',Categorydelete,name='categ-delete')
]