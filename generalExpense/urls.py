from django.urls import path
from django.views.generic import TemplateView
from generalExpense import views
urlpatterns = [
    # General Expenses
    path('expenses', views.Expenses.as_view(),name='expenses'),
    path('salaries', views.AddSalary.as_view(),name='salaries'),
    path('other_expenses', views.OtherExpenses.as_view(),name='other_expenses'),
    path('daily_expenses', views.DailyExpense.as_view(),name='daily_expenses'),
    path('constraction_and_repairs', views.Constraction.as_view(),name='constraction_and_repairs'),
    path('delete-constraction/<int:constraction_id>/', views.DeleteConstraction, name='delete-constraction'),
    path('update-constraction/<int:constraction_id>/', views.UpdateConstraction.as_view(), name='update-constraction'),
    path('delete-daily_expense/<int:daily_expense_id>/', views.DeleteDailyExpenses, name='delete-daily_expense'),
    path('update-daily_expense/<int:daily_expense_id>/', views.UpdateDailyExpense.as_view(), name='update-daily_expense'),
    path('delete-other_expense/<int:other_expense_id>/', views.DeleteOtherExpenses, name='delete-other_expense'),
    path('update-other_expense/<int:other_expense_id>/', views.UpdateOtherExpenses.as_view(), name='update-other_expense'),
    path('delete-salary/<int:salary_id>/', views.DeleteSalary, name='delete-salary'),
    path('update-salary/<int:salary_id>/', views.UpdateSalary.as_view(), name='update-salary'),


]