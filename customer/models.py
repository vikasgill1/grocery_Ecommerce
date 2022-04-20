from django.db import models
from account.models import UserAccount,UserAddress
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='customer/category/image')
    description=models.TextField(max_length=400)
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='customer/product/image')
    description=models.TextField(max_length=400)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    def __str__(self):
        return self.name

class Favorite(models.Model):
    user=models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.product.name)

class Cart(models.Model):
    user=models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.product.name)

    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price


STATUS_CHOICES=(('Accept','Accept'),('Packed','Packed'),('On The Way','On The Way'),('Delivered','Delivered'),('Cancel','Cancel'))

class Order(models.Model):
    user=models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(UserAddress,null=True,blank=True,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=30,choices=STATUS_CHOICES,default='panding')
    def __str__(self):
        return str(self.product.name)
    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price

