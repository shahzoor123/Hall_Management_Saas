from django.contrib import admin

from .models import MyProducts, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status')


@admin.register(MyProducts)
class MyProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'status')
