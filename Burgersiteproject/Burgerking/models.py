from django.db import models
from datetime import datetime,time
from .forms import User
import datetime
# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=100)
    password = models.CharField(max_length=100)






class Category(models.Model):
    name=models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.name

class Product(models.Model):
    name= models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description =models.CharField(max_length=200,default='',null=True,blank=True)
    image=models.ImageField(upload_to='products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    # @staticmethod
    # def get_all_products_by_categoryid(category_id):
    #     if category_id:
    #         return Product.objects.filter(category=category_id)
    #     else:
    #         return Product.get_all_products();



class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models. CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    # time=models.TimeField(default=time.minute)
    address=models.CharField(max_length=50,default='',blank=True)
    phone=models.CharField(max_length=10,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_history_by_user(user_id):
        return Order\
            .objects\
            .filter(user=user_id)\
            .order_by('-date')
