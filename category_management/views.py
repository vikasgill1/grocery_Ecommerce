
from django.shortcuts import render,redirect
from django.contrib import auth
from django.views import View
from category_management.forms import Categoryform
from customer.models import Category
from django.contrib import messages
# Create your views here.

def CategoryView(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            data=Category.objects.all()
            return render(request,'admin_panel/categ_mgm/categ_view.html',context={"data":data})
        else:
            auth.logout(request)
            messages.success(request, 'You have no permission access page ,only admin access this page')
            return redirect('/admin-panel/login/')

    return redirect('/admin-panel/login/')


class Category_Upadate(View):
    def get(self, request,pk):
        if request.user.is_authenticated:
            if request.user.is_superuser == True:
                stu=Category.objects.get(pk=pk)
                form=Categoryform(instance=stu)
                return render(request, 'admin_panel/categ_mgm/categ_update.html',context={'form':form})
            else:
                auth.logout(request)
                messages.success(request, 'You have no permission access page ,only admin access this page')
                return redirect('/admin-panel/login/')

        return redirect('/admin-panel/login/')

    def post(self,request,pk):
        stu=Category.objects.get(pk=pk)
        form = Categoryform(request.POST or None,request.FILES,instance=stu)
        if form.is_valid():
            form.save()
            return redirect('/admin-panel/categ-mgm/')    
        return render(request, 'admin_panel/categ_mgm/categ_Update.html',{'form':form})

class Category_add(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser == True:
                form=Categoryform()
                return render(request, 'admin_panel/categ_mgm/categ_add.html',context={'form':form})
            else:
                auth.logout(request)
                messages.success(request, 'You have no permission access page ,only admin access this page')
                return redirect('/admin-panel/login/')

        return redirect('/admin-panel/login/')

    def post(self,request):
        form = Categoryform(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin-panel/categ-mgm/')    
        return render(request, 'admin_panel/categ_mgm/categ_add.html',{'form':form})

def Categorydelete(request,pk):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            data=Category.objects.filter(pk=pk)
            data.delete()
            return redirect(request.META['HTTP_REFERER'])
        else:
            auth.logout(request)
            messages.success(request, 'You have no permission access page ,only admin access this page')
            return redirect('/admin-panel/login/')

    return redirect('/admin-panel/login/')