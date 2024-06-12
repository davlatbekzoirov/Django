from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product_mini, Product_max
from django.db.models import QuerySet
# Register your models here.
@admin.register(Product_mini)
class ProductMiniAdmin(admin.ModelAdmin):
    list_display = ['image_show', 'product_name', 'description', 'olchov', 'price', 'budget', 'material', 'status', 'kafolat']
    list_filter = ['olchov', 'status', 'kafolat']
    list_editable = ['status', 'kafolat', 'price']
    actions = ['set_som', 'set_dollars']

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='%s' width='60' />".format(obj.image.url))
        return "None"
    
    image_show.name = 'Rasm'

    @admin.action(description="Установить валюту в узбекский сум")
    def set_som(self, request, qs: QuerySet):
        qs.update(price=Product_mini.UZS)

    @admin.action(description="Установить валюту в доллар")
    def set_dollars(self, request, qs: QuerySet):
        count_updates = qs.update(price=Product_mini.USD)
        self.message_user(request, f"{count_updates} Было ")

@admin.register(Product_max)
class ProductMaxAdmin(admin.ModelAdmin):
    list_display = ['image_show', 'product_name', 'description', 'company', 'mahsulot',  'olchov', 'price', 'material', 'status', 'kafolat']
    list_filter = ['olchov', 'status', 'kafolat']
    list_editable = ['status', 'kafolat']

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='%s' width='60' />".format(obj.image.url))
        return "None"
    
    image_show.__name__ = 'Rasm'
