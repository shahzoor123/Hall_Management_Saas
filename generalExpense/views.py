from django.shortcuts import render , redirect,get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import ConstructionAndRepair, Salary, DailyExpenses, OtherExpense
from django.contrib import messages

# Create your views here.
class Expenses(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-products.html"

class AddSalary(LoginRequiredMixin,TemplateView):
    template_name = "general_expense/salary_expenses.html"
    def get(self, request):

        objects = Salary.objects.all()

        context = {
            'salaries': objects,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == "POST":
            try:
                employee_type = request.POST.get('employee-type')
                details = request.POST.get('details')
                amount = request.POST.get('amount')
                date = request.POST.get('date')
                expense_by = request.POST.get('expense-by')

                Salary.objects.create(
                    employee_type=employee_type,
                    details=details,
                    amount=amount,
                    on_date=date,
                    expense_by=expense_by
                )

                messages.success(request, "Data Added Successfully")
                return redirect('salaries')
            except:
                messages.error(request, "Erorr While updating! Please check form agian")
                return redirect('salaries')
            

def DeleteSalary(request, salary_id):
    template_name = "general_expense/salary_expenses.html"

    expense = get_object_or_404(Salary, pk=salary_id)
    # print(event.id)
    if expense is not None:
        try:
            expense.delete()
            messages.success(request, "Expense deleted successfully")
            return redirect("salaries")

        except:
            messages.error(request, "Can not delete expense")
    else:
        return redirect("salaries")

    
    objects = Salary.objects.all()

    context = {
            'salaries': objects,
        }
    
    return render(request, "general_expense/salary_expenses.html", context=context)

class UpdateSalary(LoginRequiredMixin,TemplateView):

    def get(self, request):

        objects = Salary.objects.all()

        context = {
            'salaries': objects,
        }

        return render(request, self.template_name, context)

    def post(self, request, salary_id):
        if request.method == "POST":
            try:
                requests = Salary.objects.get(id=salary_id)

                employee_type = request.POST.get('employee-type')
                details = request.POST.get('details')
                amount = request.POST.get('amount')
                date = request.POST.get('date')
                expense_by = request.POST.get('expense-by')

                # Updating old values

                requests.employee_type = employee_type
                requests.details = details
                requests.amount = amount
                requests.date = date
                requests.expense_by = expense_by

                requests.save()

                messages.success(request, "Data updated Successfully")
                return redirect('salaries')
            except:
                messages.error(request, "Erorr While updating! Please check form agian")
                return redirect('salaries')


class OtherExpenses(LoginRequiredMixin,TemplateView):
    template_name = "general_expense/other_expenses.html"

    def get(self, request):

        objects = OtherExpense.objects.all()

        context = {
            'other_expenses': objects,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == "POST":
            try:
                expense_type = request.POST.get('expense-type')
                details = request.POST.get('details')
                amount = request.POST.get('amount')
                date = request.POST.get('date')
                expense_by = request.POST.get('expense-by')

                OtherExpense.objects.create(
                    expense_type=expense_type,
                    details=details,
                    amount=amount,
                    on_date=date,
                    expense_by=expense_by
                )

                messages.success(request, "Data Added Successfully")
                return redirect('other_expenses')
            except:
                messages.error(request, "Erorr While updating! Please check form agian")
                return redirect('other_expenses')
            

def DeleteOtherExpenses(request, other_expense_id):
    template_name = "general_expense/other_expenses.html"

    expense = get_object_or_404(OtherExpense, pk=other_expense_id)
    # print(event.id)
    if expense is not None:
        try:
            expense.delete()
            messages.success(request, "Expense deleted successfully")
            return redirect("other_expenses")

        except:
            messages.error(request, "Can not delete expense")
    else:
        return redirect("other_expenses")

    
    objects = Other_expense.objects.all()

    context = {
            'other_expenses': objects,
        }
    
    return render(request, 'general_expense/other_expenses.html', context=context)

class UpdateOtherExpenses(LoginRequiredMixin,TemplateView):

    def get(self, request):

        objects = OtherExpense.objects.all()

        context = {
            'other_expenses': objects,
        }

        return render(request, self.template_name, context)

    def post(self, request, other_expense_id):
        if request.method == "POST":
            try:
                requests = OtherExpense.objects.get(id=other_expense_id)

                expense_type = request.POST.get('expense-type')
                details = request.POST.get('details')
                amount = request.POST.get('amount')
                date = request.POST.get('date')
                expense_by = request.POST.get('expense-by')

                # Updating old values

                requests.expense_type = expense_type
                requests.details = details
                requests.amount = amount
                requests.date = date
                requests.expense_by = expense_by

                requests.save()

                messages.success(request, "Data updated Successfully")
                return redirect('other_expenses')
            except:
                messages.error(request, "Erorr While updating! Please check form agian")
                return redirect('other_expenses')

                

class DailyExpense(LoginRequiredMixin,TemplateView):
    template_name = "general_expense/daily_expenses.html"

    def get(self, request):

        objects = DailyExpenses.objects.all()

        context = {
            'daily_expenses': objects,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == "POST":
            try:
                expense_type = request.POST.get('expense-type')
                details = request.POST.get('details')
                amount = request.POST.get('amount')
                date = request.POST.get('date')
                expense_by = request.POST.get('expense-by')

                DailyExpenses.objects.create(
                    expense_type=expense_type,
                    details=details,
                    amount=amount,
                    on_date=date,
                    expense_by=expense_by
                )
                messages.success(request, "Data Added Successfully")
                return redirect('daily_expenses')

            except:
                messages.error(request, "Erorr While updating! Please check form agian")
                return redirect('daily_expenses')



def DeleteDailyExpenses(request, daily_expense_id):
    template_name = "general_expense/constraction_and_repairs.html"

    expense = get_object_or_404(DailyExpenses, pk=daily_expense_id)
    # print(event.id)
    if expense is not None:
        try:
            expense.delete()
            messages.success(request, "Expense deleted successfully")
            return redirect("constraction_and_repairs")

        except:
            messages.error(request, "Can not delete expense")
    else:
        return redirect("daily_expenses")

    
    objects = DailyExpenses.objects.all()

    context = {
            'daily_expenses': objects,
        }
    
    return render(request, 'general_expense/daily_expenses.html', context=context)

class UpdateDailyExpense(LoginRequiredMixin,TemplateView):

    def get(self, request):

        objects = DailyExpenses.objects.all()

        context = {
            'daily_expenses': objects,
        }

        return render(request, self.template_name, context)

    def post(self, request, daily_expense_id):
        if request.method == "POST":
            try:
                requests = DailyExpenses.objects.get(id=daily_expense_id)

                expense_type = request.POST.get('expense-type')
                details = request.POST.get('details')
                amount = request.POST.get('amount')
                date = request.POST.get('date')
                expense_by = request.POST.get('expense-by')

                # Updating old values

                requests.expense_type = expense_type
                requests.details = details
                requests.amount = amount
                requests.date = date
                requests.expense_by = expense_by

                requests.save()
                
                messages.success(request, "Data Updated Successfully")
                return redirect('daily_expenses')
            except:
                messages.errro(request, "Erorr While updating! Please check form agian")
                return redirect('daily_expenses')

class Constraction(LoginRequiredMixin,TemplateView):
    template_name = "general_expense/constraction_and_repairs.html"

    def get(self, request):

        objects = ConstructionAndRepair.objects.all()

        context = {
            'constractions': objects,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == "POST":
            try:
                expense_for = request.POST.get('expense-for')
                details = request.POST.get('details')
                amount = request.POST.get('amount')
                date = request.POST.get('date')
                expense_by = request.POST.get('expense-by')

                ConstructionAndRepair.objects.create(
                    expense_for=expense_for,
                    details=details,
                    amount=amount,
                    on_date=date,
                    expense_by=expense_by
                )
                messages.success(request, "Data Added successfully")
                return redirect('constraction_and_repairs')
            except:
                messages.error(request, "Erorr While updating! Please check form agian")
                return redirect('constraction_and_repairs')


def DeleteConstraction(request, constraction_id):
    template_name = "general_expense/constraction_and_repairs.html"

    expense = get_object_or_404(ConstructionAndRepair, pk=constraction_id)
    # print(event.id)
    if expense is not None:
        try:
            expense.delete()
            messages.success(request, "Expense deleted successfully")
            return redirect("constraction_and_repairs")

        except:
            messages.error(request, "Can not delete expense")
    else:
        return redirect("constraction_and_repairs")

    
    objects = ConstructionAndRepair.objects.all()

    context = {
            'constractions': objects,
        }
    
    return render(request, 'general_expense/constraction_and_repairs.html', context=context)

class UpdateConstraction(LoginRequiredMixin,TemplateView):

    def get(self, request):

        objects = ConstructionAndRepair.objects.all()

        context = {
            'constractions': objects,
        }

        return render(request, self.template_name, context)

    def post(self, request, constraction_id):
        if request.method == "POST":
            requests = ConstructionAndRepair.objects.get(id=constraction_id)

            expense_for = request.POST.get('expense-for')
            details = request.POST.get('details')
            amount = request.POST.get('amount')
            date = request.POST.get('date')
            expense_by = request.POST.get('expense-by')

            # Updating old values

            requests.expense_for = expense_for
            requests.details = details
            requests.amount = amount
            requests.date = date
            requests.expense_by = expense_by

            requests.save()
            
            return redirect('constraction_and_repairs')

