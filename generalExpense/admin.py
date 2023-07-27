from django.contrib import admin
from .models import Salary, DailyExpenses, ConstructionAndRepair, OtherExpense

@admin.register(Salary)   
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee_type', 'details', 'amount', 'on_date')

@admin.register(DailyExpenses)   
class DailyExpensesAdmin(admin.ModelAdmin):
    list_display = ('expense_type', 'details', 'amount', 'on_date')

@admin.register(ConstructionAndRepair)   
class ConstructionAndRepairAdmin(admin.ModelAdmin):
    list_display = ('expense_for', 'details', 'amount', 'on_date')

@admin.register(OtherExpense)   
class OtherExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_type', 'details', 'amount', 'on_date')