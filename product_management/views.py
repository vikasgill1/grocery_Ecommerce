
from django.shortcuts import render,redirect
from django.contrib import auth
from django.views import View
from customer.models import Product
from django.contrib import messages

from product_management.forms import AdminProductForm
# Create your views here.

def AdminProductView(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            data=Product.objects.all()
            return render(request,'admin_panel/prod_mgm/prod_view.html',context={"data":data})
        else:
            auth.logout(request)
            messages.success(request, 'You have no permission access page ,only admin access this page')
            return redirect('/admin-panel/login/')

    return redirect('/admin-panel/login/')


class AdminProductUpdate(View):
    def get(self, request,pk):
        if request.user.is_authenticated:
            if request.user.is_superuser == True:
                stu=Product.objects.get(pk=pk)
                form=AdminProductForm(instance=stu)
                return render(request, 'admin_panel/prod_mgm/prod_update.html',context={'form':form})
            else:
                auth.logout(request)
                messages.success(request, 'You have no permission access page ,only admin access this page')
                return redirect('/admin-panel/login/')

        return redirect('/admin-panel/login/')

    def post(self,request,pk):
        stu=Product.objects.get(pk=pk)
        form = AdminProductForm(request.POST or None,request.FILES,instance=stu)
        if form.is_valid():
            form.save()
            return redirect('/admin-panel/prod-mgm/')    
        return render(request, 'admin_panel/categ_mgm/prod_Update.html',{'form':form})

class AdminProductAdd(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser == True:
                form=AdminProductForm()
                return render(request, 'admin_panel/prod_mgm/prod_add.html',context={'form':form})
            else:
                auth.logout(request)
                messages.success(request, 'You have no permission access page ,only admin access this page')
                return redirect('/admin-panel/login/')

        return redirect('/admin-panel/login/')

    def post(self,request):
        form = AdminProductForm(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin-panel/prod-mgm/')    
        return render(request, 'admin_panel/pro_mgm/pro_add.html',{'form':form})

def AdminProductdelete(request,pk):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            data=AdminProductForm.objects.filter(pk=pk)
            data.delete()
            return redirect(request.META['HTTP_REFERER'])
        else:
            auth.logout(request)
            messages.success(request, 'You have no permission access page ,only admin access this page')
            return redirect('/admin-panel/login/')

    return redirect('/admin-panel/login/')