from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MyProducts, Deals
from ecommerce.models import EventSale
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
        context = {}
        if request.method == "POST":
                bill_number = request.POST.get('bill-no')
                serial = request.POST.get('serial-no')

                event_status = request.POST.get('status')
                event_time = request.POST.get('event-time')

                event_date = request.POST.get('event-date')
                number_of_people = request.POST.get('no-of-people')
                setup = request.POST.get('setup')

                deal_number = request.POST.get('deals')

                deal_id = request.POST.get('deals')
                deal = Deals.objects.get(id=deal_id)
            
                customer_name = request.POST.get('customer-name')
                customer_number = request.POST.get('customer-number')
                per_head = request.POST.get('per-head')
                extra_charge = request.POST.get('extra-charges')
                food_menu = request.POST.get('food-menu')
                
                details = request.POST.get('details')
                received_ammount = request.POST.get('received-amount')

                request.session['bill-no'] = bill_number
                request.session['deals'] = deal_number

                add_event_sale = EventSale.objects.create(
                    bill_no=bill_number,
                    sr=serial,
                    status=event_status,
                    event_timing=event_time,
                    event_date=event_date,
                    no_of_people=number_of_people,
                    setup=setup,
                    deals=deal,
                    customer_name=customer_name,
                    customer_number=customer_number,
                    per_head=per_head,
                    extra_charges=extra_charge,
                    food_menu=food_menu,
                    detials=details,
                    total_amount = (int(number_of_people) * int(per_head)) + int(extra_charge),
                    recieved_amount=received_ammount, 
                    remaining_amount = ((int(number_of_people) * int(per_head)) + int(extra_charge)) - int(received_ammount)
                )
               
                bill_num = request.session.get('bill-no')
                deal_num = request.session.get('deals')
                
                print(bill_num)  
                print(deal_num)     
                
                products = MyProducts.objects.all()
                deal = get_object_or_404(Deals, pk=deal_id)
                items = MyProducts.objects.filter(deals=deal)
                

                print('done')
               
                sale = EventSale.objects.filter(bill_no=bill_num)
                 
                print(sale)
                                
                
            

                combined_data = zip(items, products)
        
                
                context = {
                    'combined_data': combined_data,
                    'sales' : sale,
                }
                # Render extras/pages/pages-invoice.html with the context
                return render(request, 'extras/pages/pages-invoice.html', context)
        
        food_list = []
        products = MyProducts.objects.all()
        deal = get_object_or_404(Deals, pk=deal_id)
        items = MyProducts.objects.filter(deals=deal)
        for item in items:
            food_list.append(item.name)
    
        food_menu = ', '.join(food_list)

        sale = EventSale.objects.all()
     

        deals = Deals.objects.all()

        combined_data = zip(items, products)
        context = {
                    'combined_data': combined_data,
                    'items' : items,
                    'product': products,
                    'Deal_name' : deal,
                    'food_menu' : food_menu,
                    'sale' : sale,
                    'deal' : deal_id
                }
        # Render items/deals-calculator.html with the context
        return render(request, 'items/deals-calculator.html', context)

        

        



        