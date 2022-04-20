from unicodedata import name
from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
from django.shortcuts import render
from .models import Product,Category,Cart,Order
from account.models import UserAccount,UserAddress

# def home(request):
#     return render(request, 'customer/home.html')

class Product_view(View):
    def get(self,request):
        pro=Product.objects.all()
        cate=Category.objects.all()
        return render(request, 'customer/home.html',context={"pro":pro,'cate':cate})


# def product_detail(request):
#     return render(request, 'customer/productdetail.html')
class Product_detail(View):
    def get(self,request,pk):
        pro=Product.objects.get(pk=pk)
        us=UserAccount.objects.get(user=request.user)
        
        cart=Cart.objects.filter(product=pro,user=us)
        return render(request,'customer/productdetail.html',context={'pro':pro,'cart':cart})

class Product_Cate_detail(View):
    def get(self,request,pk):
        id=pk
        pro=Product.objects.filter(category=pk)
        cate=Category.objects.all()
        return render(request,'customer/category.html',context={'pro':pro,'cate':cate})

class Search(View):
    def get(self,request):
        pro= Product.objects.filter(name=request.POST.get('data'))

def Add_to_cart(request,pk):
    pro=Product.objects.get(pk=pk)
    us=UserAccount.objects.get(user=request.user)
    if Cart.objects.filter(product=pro,user=us):
        Cart.objects.get(product=pro,user=us).delete()
        return redirect(request.META['HTTP_REFERER'])
    else:
        Cart(user=us,product=pro).save()
        return redirect(request.META['HTTP_REFERER'])

def CartView(request):
    us=UserAccount.objects.get(user=request.user)
    car=Cart.objects.filter(user=us)
    amount=0
    shipping=70
    total_amount=0
    if car:
        for i in car:
            tot=i.quantity*i.product.selling_price
        
            amount+=tot
        total_amount+=shipping+amount
    return render(request,'customer/addtocart.html',context={'car':car,'amount':amount,'shipping':shipping,'total_amount':total_amount})

def plus_quantity(request,pk):
    us=UserAccount.objects.get(user=request.user)
    cart=Cart.objects.filter(user=us,pk=pk)
    
    if cart:
        car=Cart.objects.get(user=us,pk=pk)
        
        print(car.quantity)
        car.quantity+=1
        car.save()
    return redirect(request.META['HTTP_REFERER'])

def minus_quantity(request,pk):
    us=UserAccount.objects.get(user=request.user)
    cart=Cart.objects.filter(user=us,pk=pk)
    if cart:
        car=Cart.objects.get(user=us,pk=pk)
        if car.quantity == 1:
            car.delete()
        else:
            car.quantity-=1
            car.save()
    return redirect(request.META['HTTP_REFERER'])








def checkout(request):
    us=UserAccount.objects.get(user=request.user)
    cart=Cart.objects.filter(user=us)
    add=UserAddress.objects.filter(user=us)
    total_amount=0
    amount=0
    shipping=0
    if cart:
        for i in cart:
            tot=i.quantity*i.product.selling_price
        
            amount+=tot
        total_amount+=shipping+amount

    return render(request, 'customer/checkout.html',context={'cart':cart,'address':add,'amount':amount,'total_amount':total_amount})

def orderPlace(request):
    cusid=request.GET.get('cusid')
    print(cusid)
    cus=UserAddress.objects.get(id=cusid)
    us=UserAccount.objects.get(user=request.user)
    cart=Cart.objects.filter(user=us)
    for i in cart:
        Order(user=us,product=i.product,customer=cus,quantity=i.quantity).save()
        i.delete()
    
    return redirect('/orders/')

def orders(request):
    us=UserAccount.objects.get(user=request.user)
    ord=Order.objects.filter(user=us)
    return render(request,'customer/orders.html',context={'ord':ord})