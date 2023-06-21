from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordSetView,PasswordChangeView
from django.urls import reverse_lazy
from ecommerce.models import EventSale
from django.shortcuts import render


class Index(LoginRequiredMixin,TemplateView):
    template_name = "index.html"
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