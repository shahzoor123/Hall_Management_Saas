from django.contrib import admin
from .models import EventExpense, EventSale

@admin.register(EventExpense)
class EventExpenseAdmin(admin.ModelAdmin):
    list_display = ('bill', 'pakwan_bill', 'diesel_ltr', 'naan_bill', 'water_bill', 'electicity', 'cold_drink_bill', 'dhobi', 'other_expense', 'bbq_price', 'waiters_bill', 'stuff_bill', 'setup_bill', 'decor_bill', 'total_expense')

# admin.site.register(EventExpense)

@admin.register(EventSale)   
class EventSaleAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'bill_no', 'status', 'event_timing', 'setup', 'total_amount', 'recieved_amount', 'remaining_amount')

