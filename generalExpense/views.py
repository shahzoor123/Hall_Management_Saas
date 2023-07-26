from django.shortcuts import render , redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.
class Expenses(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-products.html"