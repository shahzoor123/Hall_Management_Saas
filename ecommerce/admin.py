from django.contrib import admin
from .models import EventExpense, EventSale, Event, MyKitchenexpense

@admin.register(EventExpense)
class EventExpenseAdmin(admin.ModelAdmin):
    list_display = ('bill', 'expense_date', 'pakwan_bill', 'diesel_ltr', 'naan_bill', 'water_bill', 'electicity', 'cold_drink_bill', 'dhobi', 'other_expense', 'bbq_price', 'waiters_bill', 'stuff_bill', 'setup_bill', 'decor_bill', 'total_expense')

# admin.site.register(EventExpense)

@admin.register(EventSale)   
class EventSaleAdmin(admin.ModelAdmin):
    list_display = ('id','customer_name', 'event_date','bill_no', 'status', 'event_timing', 'setup', 'total_amount', 'recieved_amount', 'remaining_amount')

@admin.register(Event)   
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'start_date', 'end_date', 'event_time')

@admin.register(MyKitchenexpense)   
class MyKitchenexpenseAdmin(admin.ModelAdmin):
    list_display = ('bill', 'date', 'total_bill')


