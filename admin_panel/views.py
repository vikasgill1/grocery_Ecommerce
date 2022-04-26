import email
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from account.models import UserAccount
from django.contrib import auth
from django.views import View
from .form import *
from django.contrib import messages
# Create your views here.


def Dasboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            return render(request,'admin_panel/index.html')
        else:
            auth.logout(request)
            messages.success(request, 'You have no permission access page ,only admin access this page')
            return redirect('/admin-panel/login/')

    return redirect('/admin-panel/login/')


class AdminLoginView(View):
    def get(self,request,*args,**kwargs):
        form = LoginForm
        if request.user.is_authenticated:
            return redirect('/admin-panel/')
        return render(request, 'admin_panel/account/login.html',{'form':form})

    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST or None)
        
        if form.is_valid():
            em = request.POST['email']
            user = User.objects.get(Q(is_superuser=True) | Q(useraccount__user_type='admin'), email=em)
            
            auth.login(request,user)
            return redirect('/admin-panel/')
            
        return render(request, 'admin_panel/account/login.html',{'form':form})


class AdminLogoutView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated | request.user.is_superuser == True :
           auth.logout(request)
           return redirect('/admin-panel/login/')
        return redirect('/admin-panel/')

    

class ChangePasswordView(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser == True:
                form=MyPasswordChangeForm(user=request.user)
                return render(request, 'admin_panel/account/changepassword.html',context={'form':form})
            else:
                auth.logout(request)
                messages.success(request, 'You have no permission access page ,only admin access this page')
                return redirect('/admin-panel/login/')

        return redirect('/admin-panel/login/')

    def post(self,request,*args,**kwargs):


        user =request.user
        print('user',user)
        
        form = MyPasswordChangeForm(request.POST or None, user=user)
        if form.is_valid():
            new_password2 = form.cleaned_data.get('new_password2')
            print('new_password2',new_password2)
            user.set_password(new_password2)
            user.save()
            return redirect('/admin-panel/logout/')    
        return render(request, 'admin_panel/account/changepassword.html',{'form':form})


def AdminProfileView(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            data=UserAccount.objects.get(user=request.user)
            return render(request,'admin_panel/account/profileView.html',context={'data':data})
        else:
            auth.logout(request)
            messages.success(request, 'You have no permission access page ,only admin access this page')
            return redirect('/admin-panel/login/')

    return redirect('/admin-panel/login/')

class AdminProfileEditView(View):
    

    def get(self, request):

        if request.user.is_authenticated:
            if request.user.is_superuser == True:
                user = request.user 
        
                form = AdminProfileEditForm
                
                try:
                    userotherinfo = UserAccount.objects.get(user=user)
                    print('in try (get)',userotherinfo)
                except:
                    userotherinfo = UserAccount.objects.create(user=user)
                    print('in except (get)',userotherinfo)

                context = {
                    'form'            : form,
                    'first_name'      : user.first_name,
                    'last_name'       : user.last_name,
                    'email'           : user.email,
                    'user_other_info' : userotherinfo,
                }
                return render(request, 'admin_panel/account/profileEdit.html',context)
            else:
                auth.logout(request)
                messages.success(request, 'You have no permission access page ,only admin access this page')
                return redirect('/admin-panel/login/')

        return redirect('/admin-panel/login/')
        
    
    def post(self, request):
        user = request.user
        try:
            userotherinfo = UserAccount.objects.get(user=user)
            print('in try (post)',userotherinfo)
        except:
            userotherinfo = UserAccount.objects.create(user=user,user_type='admin')
            print('in except (post)',userotherinfo)

        form = AdminProfileEditForm(request.POST or None,request.FILES,user=request.user)

        context = {
            'form' : form,
            'first_name'      : user.first_name,
            'last_name'       : user.last_name,
            'email'           : user.email,
            'user_other_info' : userotherinfo,
            
        }

        if form.is_valid():
            data            = form.cleaned_data
            first_name      = data['first_name']
            last_name       = data['last_name']
            email           = data['email']
            mobile_number   = data['mobile_number']
            gender          = data['gender']
            date_of_birth   = data['date_of_birth']
            profile_image   = data.get('profile_image')
            

           

            user.first_name = first_name
            user.last_name  = last_name
            user.email      = email
            user.save()

            userotherinfo.mobile_number = mobile_number
            userotherinfo.gender        = gender
            userotherinfo.date_of_birth = date_of_birth
            if profile_image:
                userotherinfo.profileimg = profile_image

            userotherinfo.save()

            return redirect('/admin-panel/')    

        return render(request, 'admin_panel/account/profileEdit.html',context)
