from django.contrib import admin

from .models import Items, Category, Usage

@admin.register(Usage)
class UsageAdmin(admin.ModelAdmin):
    list_display = ('get_function_id', 'get_item', 'get_quantity_used')

    def get_function_id(self, obj):
        return obj.function.customer_name
    get_function_id.short_description = "Client's Function"

    def get_item(self, obj):
        return obj.item.name
    get_item.short_description = 'Item'

    def get_quantity_used(self, obj):
        return obj.quantity
    get_quantity_used.short_description = 'Quantity Used'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status')


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'status', 'remaining_quantity')

