from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Timeline(LoginRequiredMixin,TemplateView):
    template_name = "extras/pages/pages-timeline.html"
class Invoice(LoginRequiredMixin,TemplateView):
    template_name = "extras/pages/pages-invoice.html"
class Blankpage(LoginRequiredMixin,TemplateView):
    template_name = "extras/pages/pages-blank.html"
class Error404(LoginRequiredMixin,TemplateView):
    template_name = "extras/pages/pages-404.html"
class Error500(LoginRequiredMixin,TemplateView):
    template_name = "extras/pages/pages-500.html"
class Pricing(LoginRequiredMixin,TemplateView):
    template_name = "extras/pages/pages-pricing.html"
class Maintenance(LoginRequiredMixin,TemplateView):
    template_name = "extras/pages/pages-maintenance.html"
class Comingsoon(LoginRequiredMixin,TemplateView):
    template_name = "extras/pages/pages-comingsoon.html"
class Faqs(LoginRequiredMixin,TemplateView):
    template_name = "extras/pages/pages-faq.html"
class Lockscreen(LoginRequiredMixin,TemplateView):
    template_name = "authentication/auth-lock-screen.html"
class Login(LoginRequiredMixin,TemplateView):
    template_name = "authentication/auth-login.html"
class Register(LoginRequiredMixin,TemplateView):
    template_name = "authentication/auth-register.html"