from django.shortcuts import render , redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from items.models import MyProducts
from ecommerce.models import EventSale
from ecommerce.models import EventExpense
from items.models import Deals
import json
from django.views import View
from items.models import Deals , MyProducts
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.http import JsonResponse


# Create your views here.
class Products(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-products.html"
class ProductsDetail(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-product-detail.html"




class Eventsale(LoginRequiredMixin, View):
    template_name = "ecommerce/event-sale.html"

    def get(self, request):
        sale = EventSale.objects.all()
        deals = Deals.objects.all()
        total_sales = EventSale.objects.aggregate(total_sales=Sum('total_amount'))['total_sales']
        total_expenses = EventExpense.objects.aggregate(total_expenses=Sum('total_expense'))['total_expenses']

        total_sales = total_sales or 0
        total_expenses = total_expenses or 0

        print(total_sales)
        print(total_expenses)


        context = {
            "sales": sale,
            "deals": deals
        }
        return render(request, self.template_name, context)
    
    
    def post(self, request):
        if request.method == "POST":
            bill_number = request.POST.get('bill-no')
            serial = request.POST.get('serial-no')

            event_status = request.POST.get('status')
            event_time = request.POST.get('event-time')

            event_date = request.POST.get('event-date')
            number_of_people = request.POST.get('no-of-people')
            setup = request.POST.get('setup')

            deals = request.POST.get('deals')
            customer_name = request.POST.get('customer-name')
            customer_number = request.POST.get('customer-number')
            per_head = request.POST.get('per-head')
            extra_charge = request.POST.get('extra-charges')
            food_menu = request.POST.get('food-menu')
            details = request.POST.get('details')
            received_ammount = request.POST.get('received-amount')
            add_event_sale = EventSale.objects.create(
                bill_no=bill_number,
                sr=serial,
                status=event_status,
                event_timing=event_time,
                event_date=event_date,
                no_of_people=number_of_people,
                setup=setup,
                customer_name=customer_name,
                customer_number=customer_number,
                per_head=per_head,
                extra_charges=extra_charge,
                food_menu=food_menu,
                detials=details,
                total_amount= (int(number_of_people) * int(per_head)) + int(extra_charge),
                recieved_amount=received_ammount, 
                remaining_amount = total_amount - received_ammount
            )

        print('Posted')
        return render(request, 'items/deals-calculator')


            # x = 'Deal1'
            # if x == 'Deal1':
            #     deal = Deals.objects.get(id=1)
            #     items = x.menu_items.all()
            #     context = {
            #         'items' : items
            #     }
            #     calc_get_function = Calculate()

            #     return  calc_get_function.get_context_data(request, context)   




        

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

    def get(self, request):

        deal = request.GET.get('deals')
        no_people = request.GET.get("numberOfPeople")

        


        products = MyProducts.objects.all()
        product_json = []
        for product in products:
            product_json.append({'id': product.id, 'name': product.name, 'price': float(product.price)})
        
        deals_json = []
        deals_obj = Deals.objects.get(pk=1)
        menu_items = deals_obj.menu_items.all()

        for item in menu_items:
            deals_json.append({'id': item.id, 'name': item.name, 'price': float(item.price)})
        
        context = {
            "page_title": "Point of Sale",
            "products": products,
            "product_json": json.dumps(product_json),
            'deal_type': "custom", 
            "default_items": deals_json,
            "isCustomDeal": False,
            "deal_items": deals_json,
            "no_people": no_people
        }
        return render(request, self.template_name, context)


class DealsCalulator(LoginRequiredMixin,TemplateView):
    template_name = "items/deals-calculator.html"



class Calendar(LoginRequiredMixin,TemplateView):
    template_name = "calendar.html"
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request):
        
        if request.method == "POST":
            event_id = request.POST.get('event_name')
            event_name = EventSale.objects.get(id=event_id)
            event_start_date = request.POST.get('event_start_date')
            event_end_date = request.POST.get('event_end_date')
            event_timing = request.POST.get('event_timing') 
        
            create_event = Event.objects.create(event_title=event_name,start_date=event_start_date,end_date=event_end_date,event_time=event_timing)
            
            
            print('Posted')      

        return render(request, 'calendar.html')

        


    def get(self, request):
        event_list = []
        
        sale = EventSale.objects.all()
        events = Event.objects.all()
        
        serialized_event = serialize('json', events)
        
        data = json.loads(serialized_event)
        
        for i in data:
            event_list.append(i['fields'])
            
        
        
        event_json = json.dumps(event_list)
        print(event_json)
        
        context = {
            "events" : event_json,
            "event_sale" : sale
        }
        return render(request, 'calendar.html', {'serialized_events': serialized_event,'event_sale' : sale})
    

