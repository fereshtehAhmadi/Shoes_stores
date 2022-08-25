from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from manager.models import User
from django.core.validators import RegexValidator


class Accounts(AbstractBaseUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=10, validators=[RegexValidator(regex=r'(\d{10})$')])
    wallet = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name


class Validation(models.Model):
    phone = phone = models.CharField(max_length=11, unique=True,
                            validators=[RegexValidator(regex=r'09(\d{9})$')])
    code = models.CharField(max_length=4, blank=True, null=True)
    
    def __str__(self):
        return self.phone
