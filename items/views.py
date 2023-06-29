from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MyProducts, Deals
import json


class Calculate(LoginRequiredMixin,TemplateView):
    template_name = "items/pos.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = MyProducts.objects.filter(status=1)
        product_json = []
        for product in products:
            product_json.append({'id': product.id, 'name': product.name, 'price': float(product.price)})
        context['page_title'] = "Point of Sale"
        context['products'] = products
        context['product_json'] = json.dumps(product_json)
        return context
    

     



def item(request, deal_id):

    products = MyProducts.objects.all()

    deal = get_object_or_404(Deals, pk=deal_id)
    print(deal)
    items = MyProducts.objects.filter(deals=deal)
    
    # for i in items:
    #     print(i)
    context = {
        'items' : items,
        'product': products,
        'Deal_name' : deal,
    }
    return render(request, 'items/deals-calculator.html', context)   