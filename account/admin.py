from django.contrib import admin
from account.models import Contact

# Register your models here.

admin.site.site_header= 'Foodie | Admin'

class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','subject','is_approved']

admin.site.register(Contact ,ContactAdmin)



# class VegetarianAdmin(admin.ModelAdmin):
#     list_display=('item','price')
# admin.site.register(Vegetarian,VegetarianAdmin)

# class NonvegAdmin(admin.ModelAdmin):
#     list_display=('item','price')
# admin.site.register(Nonveg,NonvegAdmin)


# class BeverageAdmin(admin.ModelAdmin):
#     list_display=('item','price')
# admin.site.register(Beverages,BeverageAdmin)
