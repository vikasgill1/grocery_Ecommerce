from django.urls import path
from account.views import *
from django.contrib.auth import views
from .forms import Loginform,MyPasswordChangeForm,MypasswordResetform,MySetPasswordform
urlpatterns = [
    path('profileUpdate/', profileUpdate.as_view(), name='profile_update'),
    path('profileView/',ProfileView,name='profile'),
    path('registration/', CustomerRegistrationView.as_view(), name='customerregistration'),
    path('resetpassword/',views.PasswordResetView.as_view(template_name='account/resetpassword.html',form_class=MypasswordResetform), name='resetpassword'),
    path('resetpassword/done/',views.PasswordResetDoneView.as_view(template_name='account/resetpassword_done.html'), name='password_reset_done'),
    path('resetpasswordconfirm/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(template_name='account/resetpassword_confirm.html',form_class=MySetPasswordform), name='password_reset_confirm'),
    path('resetpasswordcomplete/',views.PasswordResetCompleteView.as_view(template_name='account/completeresetpassword.html'), name='password_reset_complete'),

    # path('address/', address, name='address'),
    path('login/',views.LoginView.as_view(template_name='account/login.html',authentication_form=Loginform),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('changepassword/',views.PasswordChangeView.as_view(template_name='account/changepassword.html',form_class=MyPasswordChangeForm,success_url='home'),name='changepassword'),
    path('profileUpdate/', profileUpdate.as_view(), name='profile_update'),
    path('profileView/',ProfileView,name='profile'),
    path('add-address/',Address.as_view(),name='add-address'),
    path('view-address/',addressView,name='view-address')
]
