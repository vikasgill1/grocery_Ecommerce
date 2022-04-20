
from django.shortcuts import render,redirect
from django.views import View
from .forms import CustomerRegistrationForm,Profileform,Addressform
from .models import *
from  django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request, 'account/login.html')

# def customerregistration(request):
#     return render(request, 'account/customerregistration.html')
class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm() 
        return render(request,'account/customerregistration.html',context={'form': form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'account/customerregistration.html',context={'form': form,"msg":'User Register Successfully'})
        return render(request,'account/customerregistration.html',context={'form': form})
        
        
# def profile(request):
    
#     return render(request, 'account/profile.html')
class profileUpdate(View):
    def get(self,request):
        pro=UserAccount.objects.get(user=request.user)
        us=User.objects.get(id=request.user.id)
        form=Profileform(instance= pro)
        return render(request, 'account/profileEdit.html',context={'form':form,'active':'btn btn-primary'})
    def post(self,request):
        pro=UserAccount.objects.get(user=request.user)
        form=Profileform(request.POST,instance=pro)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            gender=form.cleaned_data['gender']
            date_of_birth=form.cleaned_data['date_of_birth']
            mobile_number=form.cleaned_data['mobile_number']
            profile_image=form.cleaned_data['profile_image']
            res=UserAccount.objects.get(user=request.user)
            res.gender=gender
            res.date_of_birth=date_of_birth
            res.mobile_number=mobile_number
            res.profile_image=profile_image
            res.save()
            us=User.objects.get(id=request.user.id)
            us.first_name=first_name
            us.last_name=last_name
            us.email=email
            us.save()
           
            return render(request, 'account/profileEdit.html',context={'form':form,'active':'btn btn-primary'})
        return render(request, 'account/profileEdit.html',context={'form':form,'active':'btn btn-primary'})


def ProfileView(request):
    data=UserAccount.objects.get(user=request.user)
    return render(request, 'account/profileView.html',context={'data':data,'active':'btn btn-primary'})


class Address(View):
    def get(self,request):
        form=Addressform()
        return render(request,'account/address.html',context={'form':form,'active':'btn btn-primary'})
    def post(self,request):
        form=Addressform(request.POST)
        if form.is_valid():
            us=UserAccount.objects.get(user=request.user)
            mobile_number=form.cleaned_data['mobile_number']
            country=form.cleaned_data['country']
            state=form.cleaned_data['state']
            city=form.cleaned_data['city']
            locality=form.cleaned_data['locality']
            zipcode=form.cleaned_data['zipcode']
            address=UserAddress(user=us,mobile_number=mobile_number,country=country,state=state,city=city,locality=locality,zipcode=zipcode)
            address.save()
           
            return redirect('/account/view-address/')
        return render(request,'account/address.html',context={'form':form,'active':'btn btn-primary'})

def addressView(request):
    us=UserAccount.objects.get(user=request.user)
    print(us)
    add=UserAddress.objects.filter(user=us)
    return render(request,'account/addressView.html',context={'address':add,'active':'btn btn-primary'})


