from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ecommerce.models import EventSale

# Create your views here.
class Timeline(LoginRequiredMixin,TemplateView):
    template_name = "extras/pages/pages-timeline.html"



def order_slip(request, sale_id):
    sale = get_object_or_404(EventSale, pk = sale_id)
    # Split quantity and menu items for Invoice to show only items.
    my_menu = {}
    lst = sale.food_menu.split(',')
    # print(lst)
    for ls in lst:
        lss = ls.strip().split(' ')
        
        item = lss[0]
        my_menu.update({item: lss[1][1:-1]})

    context = {
        'sale': sale,
        'menu': my_menu
    }
    return render(request, 'extras/pages/pages-invoice.html', context)
    

class Invoice(LoginRequiredMixin,TemplateView):
    template_name = "extras/pages/invoice.html"

def sale_invoice(request, sale_id):
    
    sale = get_object_or_404(EventSale, pk=sale_id)
    status = ''
    if sale.remaining_amount == 0:
        status = "Paid"
    else:
        status = "Unpaid"

    # Split quantity and menu items for Invoice to show only items.
    my_menu = []
    lst = sale.food_menu.split(',')
    for ls in lst:
        lss = ls.strip().split(' ')
        item = lss[0]
        my_menu.append(item)
  
    stage = int(sale.stage_charges)
    entry = int(sale.entry_charges)
    extra = int(sale.extra_charges)

    total_extra_charges = stage + entry + extra

    context = {
        'sale': sale,
        'status': status,
        'food_menu': my_menu,
        'extra' : total_extra_charges,
        'sub_total' : sale.total_amount - total_extra_charges
    }

    return render(request, 'extras/pages/invoice.html', context)


class Details(LoginRequiredMixin,TemplateView):
    template_name = "extras/pages/details.html"

    def get(self, request):
        no_of_people = request.POST.get('no_of_people')
        grand_total = request.POST.get('grand_total')
        menu_items = request.POST.get('menu_items')

        return render(request, self.template_name)

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