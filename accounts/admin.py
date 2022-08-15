from django.contrib import admin
from accounts.models import Accounts, Validation


admin.site.register(Accounts)
admin.site.register(Validation)