from django.shortcuts import render , redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class Products(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-products.html"