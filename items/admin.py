from django.contrib import admin

from .models import MyProducts, Category, Deals


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status')


@admin.register(MyProducts)
class MyProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'status')


class DealsAdmin(admin.ModelAdmin):
    list_display = ('code', 'get_menu_items', 'get_total_price')

    def get_menu_items(self, obj):
        return ", ".join([item.name for item in obj.menu_items.all()])

    get_menu_items.short_description = 'Menu Items'

    def get_total_price(self, obj):
        return obj.total_price()

    get_total_price.short_description = 'Price Per Head'


admin.site.register(Deals, DealsAdmin)