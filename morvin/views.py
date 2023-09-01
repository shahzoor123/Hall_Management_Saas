from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordSetView,PasswordChangeView
from django.urls import reverse_lazy
from ecommerce.models import EventSale
from django.shortcuts import render
from ecommerce.models import EventExpense, EventSale
from django.db.models import Sum



class Index(LoginRequiredMixin,TemplateView):
    template_name = "index.html"

    def get(self, request):
        
        total_sales = EventSale.objects.aggregate(total_sales=Sum('total_amount'))['total_sales']
        total_expenses = EventExpense.objects.aggregate(total_expenses=Sum('total_expense'))['total_expenses']

        total_sales = total_sales or 0
        total_expenses = total_expenses or 0

        context = {
            "total_sales": total_sales,
            "total_expense": total_expenses,
            "fifty_sale": total_sales /2,
            "user": request.user,
            "fifty_revenue": (total_sales - total_expenses)/2,
            "revenue": total_sales - total_expenses

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