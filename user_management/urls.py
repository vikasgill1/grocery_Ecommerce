import imp
from django.urls import path
from .views import *

urlpatterns = [
    path('',AdminUserView,name='user-view'),
    path('user-update/<int:pk>/',AdminUserstatus,name="user-status"),
    path('user-delete/<int:pk>/',AdminUserprofileDelete,name="user-delete"),

]