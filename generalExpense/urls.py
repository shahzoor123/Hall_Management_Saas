from django.urls import path
from django.views.generic import TemplateView
from generalExpense import views
urlpatterns = [
    # General Expenses
    path('expenses', views.Expenses.as_view(),name='expenses'),
]