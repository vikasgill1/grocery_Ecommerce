from django import forms
from django.contrib.auth.models import User
from account.models import UserAccount
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation

from django.db.models import Q

class LoginForm(forms.Form):
    email=forms.EmailField(max_length=30, required=True,label=_('Email'),widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

    password = forms.CharField(max_length=30, required=True,label=_(' Old Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    
    def clean(self):
        email    = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        
        # user_qs = User.objects.filter(email=email,is_superuser=True)
        user_qs = User.objects.filter(Q(is_superuser=True) | Q(useraccount__user_type='admin'), email=email)
        print('user_qs',user_qs)
        if user_qs.exists():
            user_obj = user_qs.first()
            if not user_obj.check_password(password):
                print('invalid pass')
                raise forms.ValidationError('Invalid password')
        else:
            print('not exit')
            raise forms.ValidationError('User with this email does not exist')
        
        return self.cleaned_data  


class MyPasswordChangeForm(forms.Form):
    old_password=forms.CharField(max_length=30, required=True,label=_(' Old Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password1=forms.CharField(max_length=30, required=True,label=_(' New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(max_length=30, required=True,label=_(' Confirm Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MyPasswordChangeForm, self).__init__(*args, **kwargs)
    
    
    def clean(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if not self.user.check_password(old_password):
            print('valid passs')
            raise forms.ValidationError('Please provide valid old password')

        if not len(new_password1) >= 8 or not len(new_password2) >=8:
            print('8')
            raise forms.ValidationError('Password must be atleast 8 characters long') 

        if new_password1 != new_password2:
            print('same')
            raise forms.ValidationError('Both new password and confirm password must be same') 

        return self.cleaned_data 


GENDER_TYPE=(('male','male'),('female','female'),('other','other'))

class AdminProfileEditForm(forms.Form):
    first_name=forms.CharField(max_length=30, required=True,label='First Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=30, required=True,label='Last Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile_number=forms.CharField(required=True,label='Mobile Number',widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(max_length=30, required=True,label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    date_of_birth=forms.DateField(required=True,label='DOB',widget=forms.TextInput(attrs={'class':'form-control'}))
    gender=forms.ChoiceField(choices=GENDER_TYPE,required=True,label='Gender')
    profile_image=forms.ImageField()
    

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(AdminProfileEditForm, self).__init__(*args, **kwargs)

    
    def clean(self):
        first_name   = self.cleaned_data.get('first_name')
        last_name    = self.cleaned_data.get('last_name')
        mobile_number= self.cleaned_data.get('mobile_number') 
        email= self.cleaned_data.get('email') 
        date_of_birth= self.cleaned_data.get('date_of_birth') 
        gender= self.cleaned_data.get('gender') 
        profile_image   = self.cleaned_data.get('profile_image')
        print(profile_image)
        user = self.user    
        print('user',user)

        if not first_name or first_name == '':
            raise forms.ValidationError('please provide first name')

        if not last_name or last_name == '':
            raise forms.ValidationError('please provide last name')

        if not email or email == '':
            raise forms.ValidationError('please provide address')

        if not mobile_number or mobile_number == "":
            raise forms.ValidationError('please provide mobile_number')  
        if not gender or gender == "":
            raise forms.ValidationError('please provide mobile_number') 

        if not mobile_number.isdigit():
            raise forms.ValidationError('please provide valid mobile_number')

        if not date_of_birth or date_of_birth == "":
            raise forms.ValidationError('please provide country code')  

          

        check_mobile_qs = UserAccount.objects.filter(mobile_number=mobile_number,user_type="admin").exclude(user=user)
        if check_mobile_qs.exists():
            raise forms.ValidationError('user with this mobile number already exist')
        
        check_email_qs= UserAccount.objects.filter(user__email=email,user_type="admim").exclude(user=user)
        if check_email_qs.exists():
            raise forms.ValidationError("user with this mobile number already exist")
        if profile_image:
            check_profileimg_ext = str(profile_image)
            if not check_profileimg_ext.lower().endswith(('.jpg','.jpeg','.png','.gif','.bmp')):
                raise forms.ValidationError("Profile Image only allows image types of GIF, PNG, JPG, JPEG and BMP. ")
