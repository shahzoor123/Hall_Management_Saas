from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordSetView,PasswordChangeView
from django.urls import reverse_lazy
from ecommerce.models import EventSale
from django.shortcuts import render
from ecommerce.models import EventExpense, EventSale
from django.db.models import Sum
from datetime import datetime
from django.db.models import Count
from django.shortcuts import render
from ecommerce.models import Event
from generalExpense.models import Salary, OtherExpense, DailyExpenses, ConstructionAndRepair, VendorsList
from django.db.models.functions import ExtractMonth
from django.core.serializers import serialize
import json
from django.utils import timezone

class Index(LoginRequiredMixin,TemplateView):
    template_name = "index.html"

    def get(self, request):
        
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 

# Getting Total number of Sales in the current month and year
     
        # Get the current month and year
        today = datetime.now()
        current_month = today.month
        current_year = today.year

        # Filter events for the current month and year
        events_this_month = Event.objects.filter(start_date__month=current_month, start_date__year=current_year)

        # Count the number of events for the current month
        events_count_this_month = events_this_month.count()

            # Get the current year
        current_year = datetime.now().year

        # Filter events for the current year
        events_this_year = Event.objects.filter(start_date__year=current_year)

        # Count the number of events for the current year
        events_count_this_year = events_this_year.count()

        total_expenses = 0

        # Getting Total Sales and Expense
        total_sale = EventSale.objects.aggregate(total_sales=Sum('total_amount'))['total_sales']
        expenses = EventExpense.objects.aggregate(total_expenses=Sum('total_expense'))['total_expenses']
        if expenses is None:
            expenses = 0

        total_expenses += expenses 

        total_sale = total_sale or 0
        total_expenses = total_expenses or 0

        # Get the total salary amount for each employee type
        employee_type_totals = (
            Salary.objects.values('employee_type')
            .annotate(total_amount=Sum('amount'))
        )

        # Get the total salary amount for each month
        month_totals = (
            Salary.objects.annotate(month=ExtractMonth('on_date'))
            .values('month')
            .annotate(total_amount=Sum('amount'))
        )

        # Format the results for the report
        salary_report = []
        for entry in employee_type_totals:
            salary_report.append(f"{entry['employee_type']} total is {entry['total_amount']}k")

        for entry in month_totals:
            month = entry['month']
            total_amount = entry['total_amount']
            salary_report.append(f"Salary of the month {month} is {total_amount}k")

        # Print or return the salary_report as needed
        for line in salary_report:
            print(line)


        # Get the total expense amount for each expense type
        expense_type_totals = (
            OtherExpense.objects.values('expense_type')
            .annotate(total_amount=Sum('amount'))
        )

        # Get the total expense amount for each month
        month_totals = (
            OtherExpense.objects.annotate(month=ExtractMonth('on_date'))
            .values('month')
            .annotate(total_amount=Sum('amount'))
        )

        # print(expense_type_totals)
        # print(month_totals)
        # Format the results for the report
        report = []
        for entry in expense_type_totals:
            report.append(f"{entry['expense_type']} total is {entry['total_amount']}")

        for entry in month_totals:
            month = entry['month']
            total_amount = entry['total_amount']
            report.append(f"Daily Expenses of the month {month} is {total_amount}k")

        # Print or return the report as needed
        # print("Report is")
        for line in report:
            print(line)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  


        # Area Chart



        # expense_list = []
        # # Get total expenses for each month based on the EventSale's create date
        # # monthly_expenses = EventExpense.objects.values('bill').annotate(Sum('total_expense')).values('total_expense')
        # monthly_expenses = EventExpense.objects.values('bill__event_date__month').annotate(total_expense=Sum('total_expense')).order_by('bill__event_date__month')
        
        # print(monthly_expenses)
        
        # for i in monthly_expenses:
        #     expense_list.append(i.values())
        # # print(monthly_expenses, 'query') 
            
        # # print(expense_list)
        # result_list = [value for dict_values_obj in expense_list for value in dict_values_obj]
        # # print(result_list, 'expenses')

        # cleaned_expenses = []
        #         # Iterate through the list, skipping every other element (i.e., the month values)
        # for i in range(0, len(result_list), 2):
        #     expense_value = result_list[i + 1]  # Get the expense value (skip the month)
        #     cleaned_expenses.append(expense_value)

        # # print(cleaned_expenses) 
        
        current_date = datetime.now()   
        
        # Get the current month and year
        today = datetime.now()
        current_month = today.month
        current_year = today.year
        
        # Get the current year
        current_year = datetime.now().year
        
        expense_list = []
        
        # Get total expenses for each month based on the EventSale's create date
         # Query the database to get total sales for every month in the current year
        monthly_expense = EventExpense.objects.filter(expense_date__year=current_date.year).annotate(month=ExtractMonth('expense_date')) \
            .values('month') \
            .annotate(total_expense=Sum('total_expense')) \
            .order_by('month')
        
        month_expense_dict = {entry['month']: entry['total_expense'] for entry in monthly_expense}
        
           # Iterate through all 12 months
        for month in range(1, 13):
            # Check if the month is present in the dictionary
            if month in month_expense_dict:
                total_expense = month_expense_dict[month]
            else:
                total_expense = 0  # Set total expense to 0 for missing months
            expense_list.append(total_expense)

        # print(expense_list , 'expense')
    

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  

        # Dashboard cards 

        current_date = datetime.now()

        all_months = []
        all_sales_this_year = []
        total_sale_this_year = 0
        total_events = 0
        
        
        events_this_month = EventSale.objects.filter(event_date__month=current_date.month)
        events_this_year = EventSale.objects.filter(event_date__year=current_date.year)
        
        for j in events_this_year:  
            all_sales_this_year.append(j)
            total_sale_this_year = len(all_sales_this_year)
            
        # print(total_sale_this_year)    

        for i in events_this_month:  
            all_months.append(i)
            total_events = len(all_months)

        # print(total_events)


        # Montly Sales Charts
        
        
        
        
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\      



          # Query the database to get total sales for every month in the current year
        monthly_sales = EventSale.objects.filter(event_date__year=current_date.year).annotate(month=ExtractMonth('event_date')) \
            .values('month') \
            .annotate(total_sales=Sum('total_amount')) \
            .order_by('month')
            
        month_sales_dict = {entry['month']: entry['total_sales'] for entry in monthly_sales}

         # Initialize a list to store total sales for every month
        every_month_sale = []

        # Iterate through all 12 months
        for month in range(1, 13):
            # Check if the month is present in the dictionary
            if month in month_sales_dict:
                total_sales = month_sales_dict[month]
            else:
                total_sales = 0  # Set total sales to 0 for missing months
            every_month_sale.append(total_sales)

        # print(every_month_sale)
        
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\      


        
        
        # calender
        
        
        event_list = []
        
        sale = EventSale.objects.all()
        events = Event.objects.all()
        vendors = VendorsList.objects.all()

        
        serialized_event = serialize('json',events)
        
        data = json.loads(serialized_event)
        
        
        for i in data:
            event_list.append(i['fields'])
            
        
        
        event_json = json.dumps(event_list)
        
        
        
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\              
        
        
       
        # Upcomming events
        
        
        no_envent = -1    
        # Get the current date
        current_date = timezone.now().date()
        
        # Calculate the date 5 days from now
        end_date = current_date + timezone.timedelta(days=4)
        
        # Query the database for events within the next 5 days
        events = EventSale.objects.filter(event_date__range=[current_date, end_date])
        
        # print(len(events))
        
        for i in events:
            pass
            # print(i.customer_name,i.event_date)

        if len(events) == 0:
            no_envent = 0


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\        
        
        
        
        # Pie Chart For Expenses Breakdown
        
        pie_list = []
        
        first_value = 1
        
        pie_list.append(first_value)

        construction = ConstructionAndRepair.objects.filter(on_date__year=current_year, on_date__month=current_month).aggregate(amount=Sum('amount'))
        pie_list.append(construction['amount'])

        dailyexpense = DailyExpenses.objects.filter(on_date__year=current_year, on_date__month=current_month).aggregate(amount=Sum('amount'))
        pie_list.append(dailyexpense['amount'])

        otherexpense = OtherExpense.objects.filter(on_date__year=current_year, on_date__month=current_month).aggregate(amount=Sum('amount'))
        pie_list.append(otherexpense['amount'])

        event_expense = EventExpense.objects.filter(expense_date__year=current_year, expense_date__month=current_month).aggregate(total_expense=Sum('total_expense'))
        pie_list.append(event_expense['total_expense'])

        salaries = Salary.objects.filter(on_date__year=current_year, on_date__month=current_month).aggregate(amount=Sum('amount'))
        pie_list.append(salaries['amount'])

        

        context = {
            
            # sk
            'expense_heads' : pie_list,
            
            
            "expense": expense_list,
        
            'no_event' : no_envent,
            'upcoming_events': events,
            
            "events" : event_json,
            "event_sale" : sale,
            'serialized_events': serialized_event,
            
            "sale": every_month_sale,

            
            "total_events_this_month" : total_events,
            "total_events_this_year" : total_sale_this_year,
            
            # sk end
            
            
            
            #  hb
            "total_sales": total_sale,
            "total_expense": total_expenses,
            "fifty_sale": total_sale /2,
            "user": request.user,
            "fifty_revenue": (total_sale - total_expenses)/2,
            "revenue": total_sale - total_expenses,
            "events_this_month": events_count_this_month,
            "events_this_year":events_count_this_year,
            "vendors": vendors
            
            # hb end
            

        }
        return render(request, self.template_name, context)
    
    
    
class Calendar(LoginRequiredMixin,TemplateView):
    template_name = "calendar.html"

    def get(self, request):
        sale = EventSale.objects.all()
        context = {
            "sales": sale
        }
        return render(request, self.template_name, context)
    

class Chat(LoginRequiredMixin,TemplateView):
    template_name = "chat.html"
class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('index')
class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy('index')