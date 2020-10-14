from datetime import date


from django.db import models
from django.forms import DateField
from django.utils import timezone

class Register(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    NameF = models.CharField(max_length=400, default='')
    NameL= models.CharField(max_length=400, default='')
    Email = models.CharField(max_length=400, default='')
    Password = models.CharField(max_length=400, default='')
    PasswordC = models.CharField(max_length=400, default='')

class Restaurant_sales(models.Model):
    Restaurant_salesId=models.AutoField(primary_key=True)
    Dayly_E = models.CharField(max_length=400, default='')
    Monthly_E = models.CharField(max_length=400, default='')
    Weekly_E = models.CharField(max_length=400, default='')

class overall_sales(models.Model):
    SalseId=models.AutoField(primary_key=True)
    AllDayly_E = models.CharField(max_length=400, default='')
    AllMonthly_E = models.CharField(max_length=400, default='')
    AllWeekly_E = models.CharField(max_length=400, default='')
    restaurantId = models.CharField(max_length=400, default='')

class Food(models.Model):
    FoodId=models.AutoField(primary_key=True)
    FoodName= models.CharField(max_length=400, default='')
    FoodPrice = models.IntegerField(default='')
    RestaurantId = models.CharField(max_length=400, default='')

class RestaurantData(models.Model):
    RestaurantId=models.AutoField(primary_key=True)
    RestaurantName = models.CharField(max_length=400, default='')
    RestaurantAddress = models.CharField(max_length=400, default='')



class Restaurantl(models.Model):

    restaurantId = models.CharField(max_length=400, default='')
    salseId = models.CharField(max_length=400, default='')

class Product(models.Model):
    ProductName = models.CharField(max_length=300)

    ProductQty = models.CharField(max_length=300)
    ProductPrice = models.CharField(max_length=300)
    QP = models.CharField(max_length=300)

    def __str__(self):
        return self.ProductName


class Ordert(models.Model):
    OId = models.AutoField(primary_key=True)
    ODate = models.DateField(default=timezone.now)
    Allproduct = models.ManyToManyField(Product)
    TPrice = models.CharField(max_length=400, default='')
    RestaurantName=models.CharField(max_length=400, default='')


    def __str__(self):
        return self.OId







