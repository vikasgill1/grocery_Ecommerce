from django.urls import  path,include
from .views import *

urlpatterns = [
    path('', Dasboard,name='dasboard'),
    path("login/",AdminLoginView.as_view(),name="admin-login"),
    path('logout/',AdminLogoutView.as_view(),name="admin-logout"),
    path('changepassword/',ChangePasswordView.as_view(),name="admin-changepassword"),
    path('profileView/',AdminProfileView,name="admin-profileview"),
    path('profileEdit/',AdminProfileEditView.as_view(),name='admin-profile-edit'),
    path("user-mgm/",include('user_management.urls'),name='user-mgm'),
    path("categ-mgm/",include('category_management.urls'),name='categ-mgm'),
    path("prod-mgm/",include('product_management.urls'),name='prod-mgm'),
    path("ord-mgm/",include('order_management.urls'),name='ord-mgm'),
]