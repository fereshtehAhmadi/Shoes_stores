from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, User
)
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, username, name, phone, address, national_code, bank_account_number, is_admin, password=None, password2=None):
        if not first_name or not last_name or not phone:
            raise ValueError('please fill in all fields!!')

        user = self.model(
            username=username,
            name=first_name,
            phone=phone,
            address=address,
            national_code=national_code,
            bank_account_number=bank_account_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, phone, address, national_code, bank_account_number, is_admin, password=None, password2=None):
    
        user = self.create_user(
            username,
            name=first_name,
            password=password,
            phone=phone,
            address=address,
            national_code=national_code,
            bank_account_number=bank_account_number,
        )
        user.is_admin = is_admin
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11, unique=True, 
                            validators=[RegexValidator(regex=r'09(\d{9})$')])
    address = models.TextField()
    national_code = models.CharField(max_length=10)
    bank_account_number = models.CharField(max_length=24)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'phone', 'address', 'national_code', 'bank_account_number', 'is_admin']

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return True

