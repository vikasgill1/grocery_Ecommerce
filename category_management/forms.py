from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from customer.models import Category




class Categoryform(forms.ModelForm):
    name=forms.CharField(max_length=30, required=True,label='Category Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    description=forms.CharField(max_length=30, required=True,label='Description',widget=forms.TextInput(attrs={'class':'form-control'}))
    image=forms.ImageField(required=True,label='Category Image')

    class Meta:
        model=Category
        fields=('name','description','image')
