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
from generalExpense.models import Salary, OtherExpense, DailyExpenses, ConstructionAndRepair
from django.db.models.functions import ExtractMonth

class Index(LoginRequiredMixin,TemplateView):
    template_name = "index.html"

    def get(self, request):
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
        total_sales = EventSale.objects.aggregate(total_sales=Sum('total_amount'))['total_sales']
        expenses = EventExpense.objects.aggregate(total_expenses=Sum('total_expense'))['total_expenses']
        if expenses is None:
            expenses = 0

        total_expenses += expenses 

        total_sales = total_sales or 0
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




        expense_list = []
        # Get total expenses for each month based on the EventSale's create date
        # monthly_expenses = EventExpense.objects.values('bill').annotate(Sum('total_expense')).values('total_expense')
        monthly_expenses = EventExpense.objects.values('bill__event_date__month').annotate(total_expense=Sum('total_expense')).order_by('bill__event_date__month')
        for i in monthly_expenses:
            expense_list.append(i.values())
        print(monthly_expenses, 'query') 
            
        # print(expense_list)
        result_list = [value for dict_values_obj in expense_list for value in dict_values_obj]
        print(result_list, 'expenses')

        cleaned_expenses = []
                # Iterate through the list, skipping every other element (i.e., the month values)
        for i in range(0, len(result_list), 2):
            expense_value = result_list[i + 1]  # Get the expense value (skip the month)
            cleaned_expenses.append(expense_value)

        print(cleaned_expenses)    



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
        print("Report is")
        for line in report:
            print(line)


        current_date = datetime.now()

        all_months = []
        all_sales_this_year = []
        
        events_this_month = EventSale.objects.filter(event_date__month=current_date.month)
        events_this_year = EventSale.objects.filter(event_date__year=current_date.year)
        
        for j in events_this_year:  
            all_sales_this_year.append(j)
            total_sale_this_year = len(all_sales_this_year)
            
        
        
        for i in events_this_month:  
            all_months.append(i)
            total_events = len(all_months)
        


        context = {
            "expense": cleaned_expenses,
            
            
            "total_sales": total_sales,
            "total_expense": total_expenses,
            "fifty_sale": total_sales /2,
            "user": request.user,
            "fifty_revenue": (total_sales - total_expenses)/2,
            "revenue": total_sales - total_expenses,
            "events_this_month": events_count_this_month,
            "events_this_year":events_count_this_year,

            "total_events_this_month" : total_events,
            "total_events_this_year" : total_sale_this_year,

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