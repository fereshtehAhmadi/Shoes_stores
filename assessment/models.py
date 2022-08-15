from django.db import models
from accounts.models import Accounts
from shoes.models import Shoes


class Comment(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    active = models.BooleanField(default=False)
    

class Assessment(models.Model):
    NUMBER = [
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three'),
        ('4', 'four'),
        ('5', 'five'),
    ]
    assessment = models.CharField(max_length=1, choices=NUMBER)
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
