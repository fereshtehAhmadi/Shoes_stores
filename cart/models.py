from django.db import models
from accounts.models import Accounts
from shoes.models import Shoes, Color, Size, Gallery


class Timespan(models.Model):
    start = models.CharField(max_length=4)
    end = models.CharField(max_length=4)
    timespan = models.CharField(max_length=4)


class Day(models.Model):
    DAYS = [
        ('1', 'satu5rday'),
        ('2', 'sunday'),
        ('3', 'monday'),
        ('4', 'tuesday'),
        ('5', 'wednesday'),
        ('6', 'thursday'),
        ('7', 'friday'),
    ]
    day = models.CharField(max_length=1, choices=DAYS)
    
    def __str__(self):
        return self.day
    

class DeliveryTime(models.Model):
    start = models.CharField(max_length=4)
    end = models.CharField(max_length=4)
    date = models.ForeignKey(Day, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    color = models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='color')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    photo = models.ForeignKey(Gallery, on_delete=models.CASCADE)


class Reserve(models.Model):
    delivery_time = models.ForeignKey(DeliveryTime, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class MyPurchases(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='my_purchases')
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    color = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    photo = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
