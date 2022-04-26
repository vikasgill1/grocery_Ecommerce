
from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib import auth
from customer.models import Order, Product
from django.contrib import messages

# Create your views here.

def AdminOrderView(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            if request.method == 'GET' or 'alldatabtn' in request.GET:
                data=Order.objects.all()
                order='All order'
            if 'pendingbtn' in request.GET:
                data=Order.objects.filter(status='panding')
                order="pending oder"
            if 'Acceptbtn' in request.GET:
                data=Order.objects.filter(status='Accept')
                order="Accept order"
            if 'Packedbtn' in request.GET:
                data=Order.objects.filter(status='Packed')
                order="Packed ordered"
            if 'waybtn' in request.GET:
                data=Order.objects.filter(status='On The Way')
                order="On The Way Order"
            if "Deliveredbtn" in request.GET:
                data=Order.objects.filter(status="Delivered")
                order="successfully Delivered  Order"
            if "Cancelbtn" in request.GET:
                data= Order.objects.filter(status='Cancel')
                order="Cancel Ordered"

            return render(request,'admin_panel/ord_mgm/ord_view.html',context={"data":data,'order':order})
        else:
            auth.logout(request)
            messages.success(request, 'You have no permission access page ,only admin access this page')
            return redirect('/admin-panel/login/')

    return redirect('/admin-panel/login/')



def AdminOrderUpdate(request,pk):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            stu=Order.objects.get(pk=pk)
            if stu.status == 'panding':
                stu.status='Accept'
                stu.save()
                return redirect(request.META['HTTP_REFERER'])
            elif stu.status == 'Accept':
                stu.status='Packed'
                stu.save()
                return redirect(request.META['HTTP_REFERER'])
            
            elif stu.status == 'Packed':
                stu.status='On The Way'
                stu.save()
                return redirect(request.META['HTTP_REFERER'])
            elif stu.status == 'On The Way':
                stu.status='Delivered'
                stu.save()
                return redirect(request.META['HTTP_REFERER'])
            elif stu.status == 'On The Way':
                stu.status='Delivered'
                stu.save()
                return redirect(request.META['HTTP_REFERER'])
            else:
                return redirect(request.META['HTTP_REFERER'])
            
        else:
            auth.logout(request)
            messages.success(request, 'You have no permission access page ,only admin access this page')
            return redirect('/admin-panel/login/')

    return redirect('/admin-panel/login/')
   

def AdminOrderCancel(request,pk):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            if Order.objects.filter(Q(status="panding") | Q(status="Accept") | Q(status="Packed") | Q(status="On The Way"),pk=pk):
                data=Order.objects.get(pk=pk)
                data.status='Cancel'
                data.save()
                return redirect(request.META['HTTP_REFERER'])
            return redirect(request.META['HTTP_REFERER'])
        else:
            auth.logout(request)
            messages.success(request, 'You have no permission access page ,only admin access this page')
            return redirect('/admin-panel/login/')

    return redirect('/admin-panel/login/')