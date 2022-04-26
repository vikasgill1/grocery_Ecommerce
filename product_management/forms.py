from sre_parse import CATEGORIES
from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from customer.models import Category, Product




class AdminProductForm(forms.ModelForm):
    category=forms.ModelChoiceField(queryset=Category.objects.all(),label='Category Name',required=True)
    name=forms.CharField(max_length=30, required=True,label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    description=forms.CharField(max_length=30, required=True,label='Description',widget=forms.TextInput(attrs={'class':'form-control'}))
    image=forms.ImageField(required=True,label='Product Image')
    selling_price=forms.FloatField(required=True,label='Selling Price',widget=forms.TextInput(attrs={'class':'form-control'}))
    selling_price=forms.FloatField(required=True,label='Discount Price',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=Product
        fields=('category','name','description','image','selling_price','discount_price')
