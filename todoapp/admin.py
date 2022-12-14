from django.contrib import admin
from todoapp.models import Product
# Register your models here.
#syntax: admin.site.register(modelname)

#admin.site.register(Product)
#define custome filter

class MyPriceFilter(admin.SimpleListFilter):
    title="Price"
    parameter_name="By Price"

    def lookups(self,request,model_admin):
        return (('greater','Price>5000'),('lesser','Price<5000'))
    
    def queryset(self,request,queryset):
        if self.value()=="greater":
            return queryset.filter(price__gt=5000)
        elif self.value()=="lesser":
            return queryset.filter(price__lt=5000)
        else:
            return queryset.all()

class ProductAdmin(admin.ModelAdmin):

    list_display=['name','pdesc','price']
    list_filter=['is_deleted','cat',MyPriceFilter]

admin.site.register(Product,ProductAdmin)
