from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from items.models import MyProducts
from ecommerce.models import EventSale
from ecommerce.models import EventExpense
from items.models import Deals
import json
from django.views import View

# Create your views here.
class Products(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-products.html"
class ProductsDetail(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-product-detail.html"




class Eventsale(LoginRequiredMixin, View):
    template_name = "ecommerce/event-sale.html"

    def get(self, request):
        sale = EventSale.objects.all()
        context = {
            "sales": sale
        }
        return render(request, self.template_name, context)
        

class Eventexpense(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/event-expense.html"

    def get(self, request):
        expense = EventExpense.objects.all()
        # for i in get_eventsale:
        #     print(i.recieved_amount)
        # if amount == 0:
        #     payment_status = 'Unpaid'
        context = {
            "expenses": expense,
        }
        return render(request, self.template_name, context)


class ProductsCart(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-cart.html"
class ProductsCheckout(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-checkout.html"
class ProductsShops(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-shops.html"
class ProductsAddProduct(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-add-product.html"

class Calculate(LoginRequiredMixin,TemplateView):
    template_name = "items/pos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = MyProducts.objects.all()
        product_json = []
        for product in products:
            product_json.append({'id': product.id, 'name': product.name, 'price': float(product.price)})
        context['page_title'] = "Point of Sale"
        context['products'] = products
        context['product_json'] = json.dumps(product_json)

        deal = Deals.objects.first()  # Retrieve the first deal object
        menu_items = deal.menu_items.all() # Retrieve all the menu items associated with the deal

    
        return context