from django.db import models
from django.core.validators import RegexValidator


class Accounts(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11, unique=True, 
                            validators=[RegexValidator(regex=r'09(\d{9})$')])
    address = models.TextField()
    postal_code = models.CharField(max_length=10, validators=[RegexValidator(regex=r'(\d{10})$')])
    national_code = models.CharField(max_length=10, unique=True, 
                                     validators=[RegexValidator(regex=r'(\d{10})$')])
    birth_day = models.DateField()
    wallet = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
