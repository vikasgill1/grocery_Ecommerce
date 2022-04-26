from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.db.models.signals  import post_save
from django.dispatch import receiver
from .models import UserAddress,UserAccount
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation

class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField(max_length=30, required=True,label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(max_length=30, required=True,label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(max_length=30, required=True,label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(max_length=30, required=True,label='Conform Password(again))',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','email','password1','password2')

    

class Loginform(AuthenticationForm):
    username=UsernameField(max_length=30, required=True,label='Username',widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(max_length=30, required=True,label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(max_length=30, required=True,label=_(' Old Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password1=forms.CharField(max_length=30, required=True,label=_(' New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(max_length=30, required=True,label=_(' Confirm Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

class MypasswordResetform(PasswordResetForm):
    email=forms.EmailField(max_length=30, required=True,label=_('Email'),widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswordform(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
    )


GENDER_TYPE=(('male','male'),('female','female'),('other','other'))


class Profileform(forms.ModelForm):
    first_name=forms.CharField(max_length=30, required=True,label='First Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=30, required=True,label='Last Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile_number=forms.CharField(required=True,label='Mobile Number',widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(max_length=30, required=True,label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    date_of_birth=forms.DateField(required=True,label='DOB',widget=forms.TextInput(attrs={'class':'form-control'}))
    gender=forms.ChoiceField(choices=GENDER_TYPE,required=True,label='Gender')
    profile_image=forms.ImageField(required=True,label='Profile Image')

    class Meta:
        model=UserAccount
        fields=('first_name','last_name','email','gender','date_of_birth','mobile_number','profile_image')

class Addressform(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields=('mobile_number','country','state','city','locality','zipcode')