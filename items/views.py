from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MyProducts, Deals
from ecommerce.models import EventSale, Event
import json
from django.shortcuts import render , redirect,get_object_or_404
from django.contrib import messages



class Calculate(LoginRequiredMixin,TemplateView):
    template_name = "items/pos.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = MyProducts.objects.filter(status=1)
        product_json = []
        for product in products:
            product_json.append({'id': product.id, 'name': product.product_name, 'price': float(product.price)})
        context['page_title'] = "Point of Sale"
        context['products'] = products
        context['product_json'] = json.dumps(product_json)
        return context
    

     

def custom_menu(request):
        context = {}
        try:
            if request.method == "POST":
                

                    event_status = request.POST.get('status')
                    event_time = request.POST.get('event-time')

                    event_date = request.POST.get('event-date')
                    number_of_people = request.POST.get('no-of-people')
                    setup = request.POST.get('setup')

                    deal_number = request.POST.get('deals')

                    # deal_id = request.POST.get('deals')
                    # deal = Deals.objects.get(id=deal_id)

                    deal = request.POST.get('deals')
                    location = request.POST.get('location')

                
                    customer_name = request.POST.get('customer-name')
                    customer_number = request.POST.get('customer-number')
                    per_head = request.POST.get('per-head')
                    hall = request.POST.get('hall')
                    per_head = float(per_head)

                    extra_charge = request.POST.get('extra-charges')
                    stage_charge = request.POST.get('stage-charges')
                    entry_charge = request.POST.get('entry-charges')
                    
                    menu_amount = request.POST.get('menu-amount')
                    menu_amount = float(menu_amount)
                    food_menu = request.POST.get('food-menu')

                    gents = request.POST.get('gents')
                    ladies = request.POST.get('ladies')

                    details = request.POST.get('details')
                    received_ammount = request.POST.get('received-amount')

                    request.session['deals'] = deal_number
                    total = (int(number_of_people) * int(per_head)) + (int(extra_charge) + int(stage_charge) + int(entry_charge)) 
                    add_event_sale = EventSale(
                        
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
                        stage_charges= stage_charge,
                        entry_charges=entry_charge,
                        hall_charges = hall,
                        location=location,
                        gents=gents,
                        ladies= ladies,
                        total_menu= int(menu_amount),
                        food_menu=food_menu,
                        detials=details,
                        total_amount= total ,
                        recieved_amount=received_ammount, 
                        remaining_amount = total - int(received_ammount)
                    )
                    add_event_sale.save()

                    Event.objects.create(sale_id = add_event_sale, event_title=customer_name,start_date=event_date,end_date=event_date,event_time=event_time)
                    messages.success(request, "Event added Successfully")
                    return redirect('event-sale')
        except:
            
            messages.error(request, "Invalid Form Submission,  Hint: Check for empty form fields, make sure to not add text in filed of number, remove for decimal number")
            return redirect('calculate_menu')




class Pre_Deals(LoginRequiredMixin,TemplateView):
    template_name = "items/deals-calculator.html"
    
    def get(self, request, deal_id):

            food_list = []
            products = MyProducts.objects.all()
            deal = get_object_or_404(Deals, pk=deal_id)
            items = MyProducts.objects.filter(deals=deal)
            for item in items:
                food_list.append(item.product_name)
        
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
        
    
    
    def post(self, request, deal_id):
        
            
        
            context = {}
            try:
                event_status = request.POST.get('status')
                event_time = request.POST.get('event-time')

                event_date = request.POST.get('event-date')
                number_of_people = request.POST.get('no-of-people')
                setup = request.POST.get('setup')

                deal_number = request.POST.get('deals')


                deal = request.POST.get('deals')
                location = request.POST.get('location')
            
                customer_name = request.POST.get('customer-name')
                customer_number = request.POST.get('customer-number')
                per_head = request.POST.get('per-head')
                per_head = float(per_head)

                extra_charge = request.POST.get('extra-charges')
                stage_charge = request.POST.get('stage-charges')
                entry_charge = request.POST.get('entry-charges')
                hall = request.POST.get('hall')
                menu_amount = request.POST.get('menu-amount')
                menu_amount = float(menu_amount)
                food_menu = request.POST.get('food-menu')
                gents = request.POST.get('gents')
                ladies = request.POST.get('ladies')

                
                details = request.POST.get('details')
                received_ammount = request.POST.get('received-amount')

                request.session['deals'] = deal_number
                total = (int(number_of_people) * int(per_head)) + (int(extra_charge) + int(stage_charge) + int(entry_charge)) 
                add_event_sale = EventSale(
                    
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
                    total_menu = int(menu_amount),
                    hall_charges = int(hall),
                    stage_charges= stage_charge,
                    entry_charges=entry_charge,
                    location = location,
                    gents= gents,
                    food_menu=food_menu,
                    detials=details,
                    total_amount= total ,
                    recieved_amount=received_ammount, 
                    remaining_amount = total - int(received_ammount)
                )
                add_event_sale.save()
                Event.objects.create(sale_id=add_event_sale, event_title=customer_name,start_date=event_date,end_date=event_date,event_time=event_time)
                messages.success(request, "Event added Successfully")
                return redirect('event-sale')
            except:
                messages.error(request, "Invalid Form Submission,  Hint: Check for empty form fields, make sure to not add text in filed of number, remove for decimal number")
                return redirect('deals-calculator')
            
            
        
   
        
       

        

        




     
            