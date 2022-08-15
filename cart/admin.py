from django.contrib import admin
from cart.models import Timespan, Day, DeliveryTime, Cart, Reserve, MyPurchases


class TimespanAdmin(admin.ModelAdmin):
    list_display=['start', 'end', 'timespan', ]
    
admin.site.register(Timespan, TimespanAdmin)

class DeliveryTimeAdmin(admin.ModelAdmin):
    list_display=['start', 'end', 'date', ]
    
admin.site.register(DeliveryTime, DeliveryTimeAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display=['user', 'shoes', 'color', 'size', 'photo']
    
admin.site.register(Cart, CartAdmin)

class MyPurchasesAdmin(admin.ModelAdmin):
    list_display=['user', 'shoes', 'color', 'size', 'photo']
    
admin.site.register(MyPurchases, MyPurchasesAdmin)

class ReserveAdmin(admin.ModelAdmin):
    list_display=['delivery_time', 'cart']
    
admin.site.register(Reserve, ReserveAdmin)
