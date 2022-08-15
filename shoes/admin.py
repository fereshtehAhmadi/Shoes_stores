from django.contrib import admin
from shoes.models import Shoes, Attributes, Brand, Size, Color, MainCategory, SubCategory, Gallery

admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Brand)

class ColorAdmin(admin.ModelAdmin):
    list_display=['shoes', 'size', 'color', 'number']

admin.site.register(Color, ColorAdmin)

class ShoesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'obj_id': ('id', )}

admin.site.register(Shoes, ShoesAdmin)

admin.site.register(Attributes)
admin.site.register(Size)
admin.site.register(Gallery)
