from django.shortcuts import render,redirect
from account.models import UserAccount
from django.contrib import auth
from django.views import View
from .form import *
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def AdminUserView(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            data= UserAccount.objects.filter(user_type='customer')
            return render(request,'admin_panel/user_mgm/user_view.html',context={'data':data})
        else:
            auth.logout(request)
            messages.success(request, 'You have no permission access page ,only admin access this page')
            return redirect('/admin-panel/login/')

    return redirect('/admin-panel/login/')



def AdminUserstatus(request,pk):

    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            data=User.objects.get(pk=pk)
            if data.is_active == True:
                data.is_active=False
                data.save()
                return redirect(request.META['HTTP_REFERER'])
            if data.is_active == False:
                data.is_active=True
                data.save()
                return redirect(request.META['HTTP_REFERER'])
        else:
            auth.logout(request)
            messages.success(request, 'You have no permission access page ,only admin access this page')
            return redirect('/admin-panel/login/')

    return redirect('/admin-panel/login/')




def AdminUserprofileDelete(request,pk):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            data=User.objects.get(pk=pk)
            data.delete()
            return redirect(request.META['HTTP_REFERER'])
        else:
            auth.logout(request)
            messages.success(request, 'You have no permission access page ,only admin access this page')
            return redirect('/admin-panel/login/')

    return redirect('/admin-panel/login/')