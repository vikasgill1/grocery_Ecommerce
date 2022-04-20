from django.db import models
from django.contrib.auth.models import User
# Create your models here.

USER_TYPE=(('customer','customer'),('admin','admin'))
GENDER_TYPE=(('male','male'),('female','female'),('other','other'))

class UserAccount(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE)
    gender=models.CharField(max_length=10,choices=GENDER_TYPE)
    date_of_birth=models.DateField(null=True,blank=True)
    mobile_number=models.CharField(max_length=15,default="")
    profile_image=models.ImageField(upload_to='account/profile_image',default='account/profile_image',null=True)
    is_block=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    when_add = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
    	return str(self.user.username)

class UserAddress(models.Model):
    user=models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    mobile_number=models.CharField(max_length=15,default="")
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    def __str__(self):
        return str(self.country)








