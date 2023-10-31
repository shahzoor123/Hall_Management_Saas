from django.shortcuts import render , redirect,get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_GET
from django.db.models import Sum
from ecommerce.models import EventSale
from ecommerce.models import EventExpense
from ecommerce.models import MyKitchenexpense
from items.models import Deals
import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.urls import reverse
from django.views import View
from items.models import Deals , MyProducts,Brand, Unit, Inventory
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.http import JsonResponse
from items.models import Category
from datetime import datetime
from django.db.models.functions import ExtractMonth
from django.contrib import messages
from django.db import IntegrityError
from django.db import transaction

current_date = datetime.now()

# Create your views here.
class Products(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-products.html"

    def get(self, request):
        cat = Category.objects.all()
        products = MyProducts.objects.all()


       


        context = {
            "category": cat,
            "products": products,
        }
        return render(request, self.template_name, context)

class ProductsDetail(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-product-detail.html"





class ProductList(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/product_list.html"

    def get(self, request):
        myproudcts = MyProducts.objects.all()
        category = Category.objects.all()
        brand = Brand.objects.all()
        unit = Unit.objects.all()

        context = {
            "myproducts": myproudcts,
            "brands": brand,
            "category": category,
            "units": unit,
        }
        return render(request, self.template_name, context)






class HallSaleSummary(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/finance_reports/hall_sale.html"
    
    def get(self, request):

        # Query the database to get total sales for every month in the current year
        monthly_sales = EventSale.objects.filter(event_date__year=current_date.year).annotate(month=ExtractMonth('event_date')) \
            .values('month') \
            .annotate(total_sales=Sum('total_amount')) \
            .order_by('month')
            
        month_sales_dict = {entry['month']: entry['total_sales'] for entry in monthly_sales}

         # Initialize a list to store total sales for every month
        every_month_sale = []

        # Iterate through all 12 months
        for month in range(1, 13):
            # Check if the month is present in the dictionary
            if month in month_sales_dict:
                total_sales = month_sales_dict[month]
            else:
                total_sales = 0  # Set total sales to 0 for missing months
            every_month_sale.append(total_sales)

        # print(every_month_sale)

        # Define the months and days in each month
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Initialize an empty dictionary to store the data
        dailySalesData = {}

        # Loop through each month and query the data
        for i, month in enumerate(months):
            days = days_in_month[i]
            data = EventSale.objects.filter(event_date__month=i + 1).values('event_date').annotate(total_sales=Sum('total_amount')).order_by('event_date')
            sales_data = [0] * days


            for entry in data:
                # print(entry)
                day = entry['event_date'].day
                count = entry['total_sales']
                sales_data[day - 1] = count
           

            dailySalesData[month] = sales_data
                
        # print(dailySalesData)

        # Sale Table
        
        all_sale = EventSale.objects.all()

        context = {
            "sale": every_month_sale,
            "daily_sale" : json.dumps(dailySalesData),
            "sale_table" : all_sale
        }
        
        return render(request, self.template_name, context)
        


    
class HallExpenseSummary(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/finance_reports/hall_expense.html"

    def get(self, request):

       # montly expense
        expense_list = []
        
        # Get total expenses for each month based on the EventSale's create date
         # Query the database to get total sales for every month in the current year
        monthly_expense = EventExpense.objects.filter(expense_date__year=current_date.year).annotate(month=ExtractMonth('expense_date')) \
            .values('month') \
            .annotate(total_expense=Sum('total_expense')) \
            .order_by('month')
        
        month_expense_dict = {entry['month']: entry['total_expense'] for entry in monthly_expense}
        
           # Iterate through all 12 months
        for month in range(1, 13):
            # Check if the month is present in the dictionary
            if month in month_expense_dict:
                total_expense = month_expense_dict[month]
            else:
                total_expense = 0  # Set total expense to 0 for missing months
            expense_list.append(total_expense)

        # print(expense_list , 'expense')


        # Define the months and days in each month
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

 
        dailyExpenseData = {}
         # Loop through each month and query the data
        for i, month in enumerate(months):
            days = days_in_month[i]
            data = EventExpense.objects.filter(expense_date__month=i + 1).values('expense_date').annotate(total_Expense=Sum('total_expense')).order_by('expense_date')
            Expense_data = [0] * days

            for entry in data:
                day = entry['expense_date'].day
                count = entry['total_Expense']
                Expense_data[day - 1] = count

            dailyExpenseData[month] = Expense_data
                
        # print(dailyExpenseData)
        
        all_expense = EventExpense.objects.all()

   
        context = {
            "expense": expense_list,
            "daily_expense": json.dumps(dailyExpenseData),
            "expense_table" : all_expense  
        }
        
        return render(request, self.template_name, context)
    


class KitchenSaleSummary(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/finance_reports/kitchen_sale.html"
    
    def get(self, request):
              
        all_kitchen_sale = MyKitchenexpense.objects.all()

   
        context = {
         
            "kitchen_sale_table" : all_kitchen_sale  
        }
        
        return render(request, self.template_name, context)
    
    
    
    
class KitchenExpenseSummary(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/finance_reports/kitchen_expense.html"  
    
    def get(self, request):
              
        all_kitchen_sale = MyKitchenexpense.objects.all()

   
        context = {
         
            "kitchen_sale_table" : all_kitchen_sale  
        }
        
        return render(request, self.template_name, context)
    

class Summary(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/finance_reports/summaries.html"
    
          

class Eventsale(LoginRequiredMixin, View):
    template_name = "ecommerce/event-sale.html"

    def get(self, request):
        sale = EventSale.objects.all()
        deals = Deals.objects.all()
        total_sales = EventSale.objects.aggregate(total_sales=Sum('total_amount'))['total_sales']
        total_expenses = EventExpense.objects.aggregate(total_expenses=Sum('total_expense'))['total_expenses']

        total_sales = total_sales or 0
        total_expenses = total_expenses or 0

       


        context = {
            "sales": sale,
            
            "deals": deals
        }
        return render(request, self.template_name, context)
    

def delete_sale(request, sale_id):
    
    sales = get_object_or_404(EventSale, pk=sale_id)
    event = get_object_or_404(Event, pk=sales.id)
    # print(event.id)
    if sales is not None:
        try:
            sales.delete()
            event.delete()
        except IntegrityError as e:
            error_message = str(e)
            if "Cannot delete some instances of model 'EventSale'" in error_message:
                messages.error(request, "Cannot delete due to related objects. Hint: Check for any expense relatd to sale you are deleting, Delete them first. ")
    else:
        return redirect("event-sale")

    sale = EventSale.objects.all()
    deals = Deals.objects.all()


    context = {
            "sales": sale,
            
            "deals": deals
        }
    
    return render(request, 'ecommerce/event-sale.html', context=context)

class Kitchensale(LoginRequiredMixin, View):
    template_name = "ecommerce/kitchen-sale.html"

    def get(self, request):
        sale = EventSale.objects.all()
        deals = Deals.objects.all()
        total_sales = EventSale.objects.aggregate(total_sales=Sum('total_amount'))['total_sales']
        total_expenses = EventExpense.objects.aggregate(total_expenses=Sum('total_expense'))['total_expenses']

        total_sales = total_sales or 0
        total_expenses = total_expenses or 0

       


        context = {
            "sales": sale,
            
            "deals": deals
        }
        return render(request, self.template_name, context)
    
  
class Kitchenexpense(LoginRequiredMixin, View):
    template_name = "ecommerce/kitchen-expense.html"

    def get(self, request):
        sale = EventSale.objects.all()
        deals = Deals.objects.all()
        kitchen_expense = MyKitchenexpense.objects.all()
        total_sales = EventSale.objects.aggregate(total_sales=Sum('total_amount'))['total_sales']
        total_expenses = EventExpense.objects.aggregate(total_expenses=Sum('total_expense'))['total_expenses']

        total_sales = total_sales or 0
        total_expenses = total_expenses or 0

       


        context = {
            "sales": sale,
            
            "deals": deals,

            "kitchen_expense" : kitchen_expense
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        if request.method == "POST":
            bill_num = request.POST.get('bill')
            payment = request.POST.get('payment-details')

            date = request.POST.get('date')
            mutton = request.POST.get('mutton')

            chicken = request.POST.get('chicken')
            beef = request.POST.get('beef')
            rice = request.POST.get('rice')

            dahi = request.POST.get('dahi')
            doodh = request.POST.get('doodh')
            sabzi = request.POST.get('sabzi')
            fruits = request.POST.get('fruits')

            khoya_paneer = request.POST.get('khoya-paneer')
            dry = request.POST.get('dry-fruits')
            oil = request.POST.get('oil')
            other = request.POST.get('other-items-bill')
            other_desc = request.POST.get('other-items-desc')

            
            # Fetch the EventSale object based on the provided bill_num
            try:
                event_sale = EventSale.objects.get(id=bill_num)
            except EventSale.DoesNotExist:
                # Handle the case where the EventSale with the given ID doesn't exist
                # You can return an error message or redirect to an error page
                pass
            else:
                # Create the Kitchenexpense object using the EventSale object
                total=int(mutton) + int(chicken) + int(beef) + int(rice) + int(rice) + int(dahi) + int(doodh) + int(sabzi) + int(fruits) + int(khoya_paneer) + int(oil) + int(other) + int(dry)
                add_kitchen_expense = MyKitchenexpense.objects.create(
                    bill=event_sale,  # Use the EventSale object
                    customer_name = event_sale.customer_name,
                    date=date,
                    payment_details=payment,
                    mutton=mutton,
                    chicken=chicken,
                    beef=beef,
                    rice=rice,
                    dahi=dahi,
                    doodh=doodh,
                    sabzi=sabzi,
                    fruits=fruits,
                    dry_fruits = dry,
                    khoya_cream_paneer=khoya_paneer,
                    oil=oil,
                    other_items_bill=other,
                    other_items_desc=other_desc,
                    total_bill= total
                )

        return redirect('kitchen-expense')

class KitchenexpenseUpdate(LoginRequiredMixin, View):
    template_name = "ecommerce/kitchen-expense.html"

    def get(self, request):
        sale = EventSale.objects.all()
        deals = Deals.objects.all()
        kitchen_expense = MyKitchenexpense.objects.all()
        total_sales = EventSale.objects.aggregate(total_sales=Sum('total_amount'))['total_sales']
        total_expenses = EventExpense.objects.aggregate(total_expenses=Sum('total_expense'))['total_expenses']

        total_sales = total_sales or 0
        total_expenses = total_expenses or 0

       


        context = {
            "sales": sale,
            
            "deals": deals,

            "kitchen_expense" : kitchen_expense
        }
        return render(request, self.template_name, context)
    
    def post(self, request,kitchen_expense_id):
        if request.method == "POST":
            requests = MyKitchenexpense.objects.get(id=kitchen_expense_id)

            print("I am here")
            bill_num = request.POST.get('bill')
            payment = request.POST.get('payment-details')

            date = request.POST.get('date')
            mutton = request.POST.get('mutton')

            chicken = request.POST.get('chicken')
            beef = request.POST.get('beef')
            rice = request.POST.get('rice')

            dahi = request.POST.get('dahi')
            doodh = request.POST.get('doodh')
            sabzi = request.POST.get('sabzi')
            fruits = request.POST.get('fruits')

            khoya_paneer = request.POST.get('khoya-paneer')
            dry = request.POST.get('dry-fruits')
            oil = request.POST.get('oil')
            other = request.POST.get('other-items-bill')
            other_desc = request.POST.get('other-items-desc')

            
            # Fetch the EventSale object based on the provided bill_num
            try:
                event_sale = EventSale.objects.get(id=bill_num)
            except EventSale.DoesNotExist:
                # Handle the case where the EventSale with the given ID doesn't exist
                # You can return an error message or redirect to an error page
                pass
            else:
                # Create the Kitchenexpense object using the EventSale object
                total=int(mutton) + int(chicken) + int(beef) + int(rice) + int(rice) + int(dahi) + int(doodh) + int(sabzi) + int(fruits) + int(khoya_paneer) + int(oil) + int(other) + int(dry)
                
                requests.bill=event_sale,  # Use the EventSale object
                requests.customer_name = event_sale.customer_name,
                requests.date=date,
                requests.payment_details=payment,
                requests.mutton=mutton,
                requests.chicken=chicken,
                requests.beef=beef,
                requests.rice=rice,
                requests.dahi=dahi,
                requests.doodh=doodh,
                requests.sabzi=sabzi,
                requests.fruits=fruits,
                requests.dry_fruits = dry,
                requests.khoya_cream_paneer=khoya_paneer,
                requests.oil=oil,
                requests.other_items_bill=other,
                requests.other_items_desc=other_desc,
                requests.total_bill= total
                requests.save()

                return redirect('kitchen-expense')
                

        return render(request, "ecommerce/kitchen-expense.html")

def delete_kitchen_expense(request, kitchen_expense_id):
    

    expense = get_object_or_404(MyKitchenexpense, pk=kitchen_expense_id)
    # print(event.id)
    if expense is not None:
        try:
            expense.delete()
            messages.success(request, "Deleted Successfully")
            return redirect("kitchen-expense")


        except IntegrityError as e:
            error_message = str(e)
            if "Cannot delete some instances of model 'EventSale'" in error_message:
                messages.error(request, "Cannot delete due to related objects. Hint: Check for any expense relatd to sale you are deleting, Delete them first. ")
    else:
        return redirect("kitchen-expense")

    sale = EventSale.objects.all()
    deals = Deals.objects.all()
    kitchen_expense = MyKitchenexpense.objects.all()
    context = {
            "sales": sale,
            
            "deals": deals,

            "kitchen_expense" : kitchen_expense
        }
    
    return render(request, 'ecommerce/kitchen-expense.html', context=context)

def DeleteProducts(request, product_id):
        
    product = get_object_or_404(MyProducts, pk=product_id)
    # print(event.id)
    if product is not None:
        product.delete()
        return redirect("ecommerce-product-list")

    
    category = Category.objects.all()
    brand = Brand.objects.all()
    unit = Unit.objects.all()
    products = MyProducts.objects.all()
    
    context = {
        "category": category,
        "brands": brand,
        "units": unit,
        "products": products
    }
    return render(request, "ecommerce/product_list.html", context = context)

class UpdateEventsale(LoginRequiredMixin, View):
    template_name = "ecommerce/event-sale.html"

    def get(self, request):
        sale = EventSale.objects.all()
        deals = Deals.objects.all()
        total_sales = EventSale.objects.aggregate(total_sales=Sum('total_amount'))['total_sales']
        total_expenses = EventExpense.objects.aggregate(total_expenses=Sum('total_expense'))['total_expenses']

        total_sales = total_sales or 0
        total_expenses = total_expenses or 0

       


        context = {
            "sales": sale,
            
            "deals": deals
        }
        return render(request, self.template_name, context)
    
    
    def post(self, request, sale_id):
        if request.method == "POST":

            # Updating Sales
            requests = EventSale.objects.get(id=sale_id)

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
            stage_charges = request.POST.get('stage-charges')
            entry_charges = request.POST.get('entry-charges')
            hall_charges = request.POST.get('hall-charges')

            food_menu = request.POST.get('food-menu')
            details = request.POST.get('details')
            received_ammount = request.POST.get('received-amount')

            print(number_of_people, per_head)
            total = (int(number_of_people) * int(per_head)) + (int(extra_charge) + int(stage_charges) + int(entry_charges)) 
            print(total)

            payments_details = ''
            if not received_ammount == "0":
                now = datetime.now()
                formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
                
                requests.payment_count = requests.payment_count + 1
                payments_details = f"\n{requests.payment_count}: was {received_ammount}. Change date was: {formatted_date}"

            



            requests.bill_no = bill_number
            requests.sr = serial

            requests.status = event_status
            requests.event_timing = event_time

            requests.event_date = event_date
            requests.no_of_people = number_of_people
            requests.setup = setup

            requests.customer_name = customer_name
            requests.customer_number = customer_number
            # print(requests.deals)
            # deal = get_object_or_404(Deals, pk=requests.deals)
            # requests.deals = deal
            if len(payments_details) > 1:
                requests.payment_details = requests.payment_details + payments_details

            requests.per_head = per_head
            
            requests.extra_charges = extra_charge
            requests.stage_charges = stage_charges
            requests.entry_charges = entry_charges
            requests.hall_charges = hall_charges
            

            requests.food_menu = food_menu
            requests.details = details
            new_rec_amount = requests.recieved_amount + int(received_ammount)
            requests.recieved_amount = new_rec_amount
            requests.total_amount = total

            requests.remaining_amount = int(total)  - int(new_rec_amount)

            requests.save()

            # Updating Events
            e_requests = Event.objects.get(id=sale_id)
            e_requests.event_title = customer_name
            e_requests.start_date = event_date
            e_requests.end_date = event_date
            e_requests.event_time = event_time
            e_requests.save()

            
        
            

        return redirect('event-sale')

 
 
 
 
 

class UpdateEventExpense(LoginRequiredMixin, View):
    template_name = "ecommerce/event-expense.html"

    
    
    def post(self, request, expense_id):
        try:
            if request.method == "POST":
                
                requests = EventExpense.objects.get(id=expense_id)

                
                bill = request.POST.get('bill')
                bill_number = get_object_or_404(EventSale, bill_no=int(bill))
                customer_name = bill_number.customer_name
                pakwan = int(request.POST.get('pakhwan'))

                electicity = request.POST.get('electicity-bill')
                naan =int(request.POST.get('naan-qty'))
                
            
                drinks = int(request.POST.get('cold-drinks'))
                drinks_type = request.POST.get('cold-drinks-type')


                water = int(request.POST.get('water-bottles'))
                water_type = request.POST.get('water-bottles-type')

                bbqs = int(request.POST.get('bbq-qty'))
                bbq_type = request.POST.get('bbq-type')

                diesel = request.POST.get('diesel-ltr')
                no_of_waiters = request.POST.get('no-of-waiters')
                dhobi = request.POST.get('dhobi')
                stuff = request.POST.get('stuff')

                other_expenses = request.POST.get('other-expense')

                expense_details = request.POST.get('expense-details')
            
                setup = request.POST.get('setup-bill')
                decor = request.POST.get('decore-details')
                decor_bill = request.POST.get('decor-bill')

                # try:
                nan = MyProducts.objects.get(product_name='Naan')
                naan_price = nan.price * naan




                drink = 0
                if drinks_type == 'Cold Drinks 1.5L':
                    drink = MyProducts.objects.get(product_name='Cold_Drinks_1.5L')


                elif drinks_type == "Cold Drinks Tin":
                    drink = MyProducts.objects.get(product_name='Cold_Drinks_Tin')
                    

                
                elif drinks_type == "Cold Drinks 2.5L":
                    drink = MyProducts.objects.get(product_name='Cold_Drinks_2.5L')
                    


                else:
                    drink = 0

                if not drink == 0 :
                    drink = drink.price * drinks

                
                bottles = 0
                if water_type == 'Water 1.5L':
                    bottles = MyProducts.objects.get(product_name='Water_1.5L')

                elif water_type == "Water 500ML":
                    bottles = MyProducts.objects.get(product_name='Water_500ML')

                elif water_type == "Water 300ML":
                    bottles = MyProducts.objects.get(product_name='Water_300ML')

                else:
                    bottles = 0
                
                if not bottles == 0 :
                    bottles = bottles.price * water
                
                # bbqs = MyProducts.objects.get(product_name="BBQ")
                # bbq_price = bbq * bbqs.price

                bbq = 0
                if bbq_type == 'Reshmi Kabab':
                    bbq = MyProducts.objects.get(product_name='Reshmi_Kabab')

                elif bbq_type == "Chicken Achari Boti":
                    bbq = MyProducts.objects.get(product_name='Chicken_Achari_Boti')

                elif bbq_type == "Seekh Kabab":
                    bbq = MyProducts.objects.get(product_name='Seekh_Kabab')

                elif bbq_type == "Malai Boti":
                    bbq = MyProducts.objects.get(product_name='Malai_Boti')

                else:
                    bbq = 0
                
            
                if not bbq == 0 :
                    bbq = bbqs * bbq.price

                wait = MyProducts.objects.get(product_name="Waiters")
                waiters = wait.price * int(no_of_waiters)

                pakwan = int(pakwan)
                electicity = int(electicity)
                naan_price = int(naan_price)
                drink = int(drink)
                bottles = int(bottles)
                bbq_price = int(bbq)
                diesel = int(diesel)
                waiters = int(waiters)
                stuff = int(stuff)
                dhobi = int(dhobi)
                other_expenses = int(other_expenses)
                setup = int(setup)
                decor_bill = int(decor_bill)
                # print(pakwan, naan_price, drink, bottles, bbq_price, diesel, waiters, stuff, dhobi, other_expenses, setup, decor_bill)


                total = pakwan + electicity + naan_price + bottles + drink + bbq_price + diesel + waiters + stuff + dhobi + other_expenses + setup + decor_bill

                requests.customer_name = customer_name
                requests.electicity = electicity
                requests.naan_qty = naan
                requests.naan_bill = naan_price
                requests.cold_drink_type = drinks_type
                requests.cold_drink = drinks
                requests.cold_drink_bill = drink
                requests.water_bottles_type = water_type
                requests.water = water
                requests.water_bill = bottles
                requests.bbq_type = bbq_type
                requests.bbq_kg_qty = bbqs
                requests.bbq_price = bbq
                requests.diesel_ltr = diesel
                requests.no_of_waiters = no_of_waiters
                requests.waiters_bill = waiters
                requests.dhobi = dhobi
                requests.other_expense = other_expenses
                requests.other_expense_detals = expense_details
                requests.setup_bill = setup
                requests.decor = decor
                requests.decor_bill = decor_bill
                requests.total_expense = total
            
                requests.save()
                messages.success(request, "Expense Updated Successfully.")
                return redirect('event-expense') 
        except:
            messages.error(request, "Error While updating expense. Please check form submission again.")
            return redirect('event-expense') 
 
 
   

   
        

class Eventexpense(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/event-expense.html"

    def get(self, request):
        expense = EventExpense.objects.all()
        
        events = EventSale.objects.all()

        # if len(expense):
        total_expenses = EventExpense.objects.aggregate(
            total_deisel = Sum('diesel_ltr'),
            total_electricity = Sum('electicity'),
            total_pakwan=Sum('pakwan_bill'),
            total_naan=Sum('naan_bill'),
            total_cold_drink=Sum('cold_drink_bill'),
            total_water=Sum('water_bill'),
            total_bbq_price=Sum('bbq_price'),
            total_waiters_bill=Sum('waiters_bill'),
            total_stuff_bill=Sum('stuff_bill'),
            total_dhobi=Sum('dhobi'),
            total_other_expense=Sum('other_expense'),
            total_setup_bill=Sum('setup_bill'),
            total_decore_bill=Sum('decor_bill'),
            total_expense=Sum('total_expense')
        )

        # Access the sums for each field
        total_pakwan = total_expenses['total_pakwan']
        total_naan = total_expenses['total_naan']
        total_cold_drink = total_expenses['total_cold_drink']
        total_water = total_expenses['total_water']
        total_bbq_price = total_expenses['total_bbq_price']
        total_waiters_bill = total_expenses['total_waiters_bill']
        total_stuff_bill = total_expenses['total_stuff_bill']
        total_dhobi = total_expenses['total_dhobi']
        total_other_expense = total_expenses['total_other_expense']
        total_setup_bill = total_expenses['total_setup_bill']
        total_decore_bill = total_expenses['total_decore_bill']
        total_total_expense = total_expenses['total_expense']
        total_electricity = total_expenses['total_electricity']
        total_diesel = total_expenses['total_deisel']
        context = {
            "expenses": expense,
            "events": events,
            "electricity": total_electricity,
            "diesel": total_diesel,
            "pakwan": total_pakwan,
            "naan": total_naan,
            'cold_drink': total_cold_drink, 
            "water": total_water,
            "bbq": total_bbq_price,
            "waiters": total_waiters_bill,
            "stuff": total_stuff_bill,
            "dhobi": total_dhobi,
            "other_expenses": total_other_expense,
            "setup": total_setup_bill,
            "decor": total_decore_bill,
            "total": total_total_expense,
            "len_expense" : len(expense)
        }
        return render(request, self.template_name, context)

    @transaction.atomic
    def post(self, request):
        # try: 
            bill = request.POST.get('bill-no')
            bill_number = get_object_or_404(EventSale, pk=bill)
            customer_name = bill_number.customer_name
            pakwan = int(request.POST.get('pakwan-bill'))

            electicity = request.POST.get('electicity-bill')
            naan =int(request.POST.get('naan-qty'))
            
        
            drinks = int(request.POST.get('cold-drinks'))
            drinks_type = request.POST.get('cold-drinks-type')


            water = int(request.POST.get('water-bottles'))
            water_type = request.POST.get('water-bottles-type')

            bbqs = int(request.POST.get('bbq-qty'))
            bbq_type = request.POST.get('bbq-type')

            diesel = request.POST.get('diesel-ltr')
            no_of_waiters = request.POST.get('no-of-waiters')
            dhobi = request.POST.get('dhobi')
            stuff = request.POST.get('stuff')

            other_expenses = request.POST.get('other-expense')

            expense_details = request.POST.get('expense-details')
           
            setup = request.POST.get('setup-bill')
            decor_details = request.POST.get('decore-details')
            decor_bill = request.POST.get('decor-bill')
    
            # try:
            nan = MyProducts.objects.get(product_name='Naan')
            naan_price = nan.price * naan




            drink = 0
            if drinks_type == 'Cold Drinks 1.5L':
                drink = MyProducts.objects.get(product_name='Cold_Drinks_1.5L')


            elif drinks_type == "Cold Drinks Tin":
                drink = MyProducts.objects.get(product_name='Cold_Drinks_Tin')
                

            
            elif drinks_type == "Cold Drinks 2.5L":
                drink = MyProducts.objects.get(product_name='Cold_Drinks_2.5L')
                


            else:
                drink = ''
                
            
            if not drink == '' :
                drink = drink.price * drinks

            
            bottles = 0
            if water_type == 'Water 1.5L':
                bottles = MyProducts.objects.get(product_name='Water_1.5L')

            elif water_type == "Water 500ML":
                bottles = MyProducts.objects.get(product_name='Water_500ML')

            elif water_type == "Water 300ML":
                bottles = MyProducts.objects.get(product_name='Water_300ML')

            else:
                bottles = ''
            
            if not bottles == '' :
                bottles = bottles.price * water
            
            # bbqs = MyProducts.objects.get(product_name="BBQ")
            # bbq_price = bbq * bbqs.price

            bbq = 0
            if bbq_type == 'Reshmi Kabab':
                bbq = MyProducts.objects.get(product_name='Reshmi_Kabab')

            elif bbq_type == "Chicken Achari Boti":
                bbq = MyProducts.objects.get(product_name='Chicken_Achari_Boti')

            elif bbq_type == "Seekh Kabab":
                bbq = MyProducts.objects.get(product_name='Seekh_Kabab')

            elif bbq_type == "Malai Boti":
                bbq = MyProducts.objects.get(product_name='Malai_Boti')

            else:
                bbq = 0
            
            if not bbq == 0 :
                bbq = bbqs * bbq.price

            wait = MyProducts.objects.get(product_name="Waiters")
            waiters = wait.price * int(no_of_waiters)

            pakwan = int(pakwan)
            naan_price = int(naan_price)
            drink = int(drink)
            bottles = int(bottles)
            bbq_price = int(bbq)
            diesel = int(diesel)
            waiters = int(waiters)
            stuff = int(stuff)
            dhobi = int(dhobi)
            other_expenses = int(other_expenses)
            setup = int(setup)
            decor_bill = int(decor_bill)
            


            total = pakwan + naan_price + bottles + drink + bbq_price + diesel + waiters + stuff + dhobi + other_expenses + setup + decor_bill
            if EventExpense.objects.filter(bill=bill_number).exists():
                    messages.error(request, "Sorry! This Expense already Exists")
                    return redirect('event-expense')

            
            else:

                add_event_expense = EventExpense.objects.create(
                        bill=bill_number,
                        customer_name = customer_name,
                        pakwan_bill=str(pakwan),
                        electicity = str(electicity),
                        naan_qty =  str(naan),
                        cold_drink= str(drinks),
                        water = str(water),
                        bbq_kg_qty=str(bbqs),
                        naan_bill=str(naan_price),
                        cold_drink_bill=str(drink),
                        cold_drink_type = drinks_type,
                        water_bill=str(bottles),
                        water_bottles_type=water_type,
                        bbq_price=str(bbq_price),
                        bbq_type = bbq_type,
                        diesel_ltr=str(diesel),
                        no_of_waiters= str(no_of_waiters),
                        waiters_bill=str(waiters),
                        stuff_bill=str(stuff),
                        dhobi=str(dhobi),
                        other_expense = other_expenses,
                        other_expense_detals= expense_details,
                        setup_bill=str(setup),
                        decor= decor_details,
                        decor_bill=str(decor_bill),
                        total_expense = str(total)
                    )
                messages.success(request, "Expense Added Successfully")
                return redirect('event-expense')

        # except:
        #     messages.error(request, "Invalid form! Please check form submission again.")
        #     return redirect('event-expense')
            
            
            
def DeleteExpense(request, expense_id):
        
    expense = get_object_or_404(EventExpense, pk=expense_id)
    try:
        if expense is not None:
            expense.delete()
            messages.success(request, "Expense Deleted Successfully")
            return redirect("event-expense")
    except:
        messages.error(request, "Error while deletion")
        return redirect("event-expense")
        
    expense = EventExpense.objects.all()
    
    context = {
        "expenses": expense,
    }
    return render(request, "ecommerce/event-expense.html", context = context)         
            
            
            

class ProductsAddCategory(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/category_list.html"
    
    def get(self, request):
        category = Category.objects.all()

        context = {
            "category": category,

        }
        return render(request, self.template_name, context)
   
    def post(self, request):
        try:
            if request.method == "POST":
                
                cat_name = request.POST['categoryname']
                cat_dsc = request.POST['categorydesc']
                if Category.objects.filter(name=cat_name).exists():
                    messages.error(request, "That Category already Exists")
                    return redirect('ecommerce_add_category')
            
                else:

                    Category.objects.create(
                        name = cat_name,
                        description = cat_dsc,
                    )
            messages.success(request, "Category Added Successfully")
            return redirect('ecommerce_add_category')
        except:
            messages.error(request, "Invalid Form! please check submission again.")
            return redirect('ecommerce_add_category')

class UpdateCategory(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/category_list.html"

    def post(self, request, category_id):
        try:
            if request.method == "POST":
                requests = Category.objects.get(id=category_id)

                cat_name = request.POST['categoryname']
                cat_dsc = request.POST['categorydesc']
                # print(cat_name, cat_dsc, requests.name, requests.discription)
                requests.name = cat_name
                requests.description = cat_dsc

                requests.save()
                messages.success(request, "Category Updated Successfully")
                return redirect("ecommerce_add_category")
        except:
            messages.error(request, "Error while updating Category")
            return redirect("ecommerce_add_category")


def DeleteCategory(request, category_id):
        
    category = get_object_or_404(Category, pk=category_id)
    try:
        if category is not None:
            category.delete()
            messages.success(request, "Category Deleted Successfully")
            return redirect("ecommerce_add_category")
    except:
        messages.error(request, "Error while deletion")
        return redirect("ecommerce_add_category")
        
    cat = Category.objects.all()
    
    context = {
        "category": cat,
    }
    return render(request, "ecommerce/category_list.html", context = context)


class ProductsCheckout(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-checkout.html"
class ProductsShops(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-shops.html"

class ProductsAddUnit(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/units_list.html"
    def get(self, request):
        units = Unit.objects.all()

        context = {
            "units": units,
        }
        return render(request, self.template_name, context)
    def post(self, request):
        try:
            if request.method == "POST":
                name = request.POST.get('name')
                shortname = request.POST.get('shortname')
                unit = request.POST.get('unit')

                if Unit.objects.filter(name=name).exists():
                    messages.error(request, "That Unit already Exists")
                    return redirect('ecommerce_add_unit')
            
                else:

                    Unit.objects.create(
                        name= name,
                        short_name = shortname,
                        unit = unit,
                    )
            messages.success(request, "Unit added Successfully")
            return redirect('ecommerce_add_unit')
        except:
            messages.error(request, "Invalid Form Submission, Try again with correct data")
            return redirect('ecommerce_add_unit')


class UpdateUnit(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/units_list.html"

    def post(self, request, unit_id):
        try:
            if request.method == "POST":
                requests = Unit.objects.get(id=unit_id)

                name = request.POST.get('name')
                shortname = request.POST.get('shortname')
                unit = request.POST.get('unit')

                requests.name = name
                requests.short_name = shortname
                requests.unit = unit

                requests.save()
                messages.success(request, "Unit Updated Successfully")
        except:
            messages.error(request, "Error while updating")
            return redirect('ecommerce_add_unit')



           
        return redirect('ecommerce_add_unit')

def DeleteUnit(request, unit_id):
        
    unit = get_object_or_404(Unit, pk=unit_id)
    try:
        if unit is not None:
            unit.delete()
            messages.success(request, "Unit Deleted Successfully")
            return redirect("ecommerce_add_unit")
    except:
        messages.error(request, "Error while deletion")
        return redirect("ecommerce_add_unit")
        
    unit = Unit.objects.all()
    
    context = {
        "units": unit,
    }
    return render(request, "ecommerce/product_list.html", context = context)

class ProductsAddBrand(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/brands_list.html"

    def get(self, request):
        brand = Brand.objects.all()

        context = {
            "brands": brand
        }
        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get('name')

            desc = request.POST.get('desc')

            if Brand.objects.filter(name=name).exists():
                messages.error(request, "That Brand already Exists")
                return redirect('ecommerce_add_brand')
            
            else:

                Brand.objects.create(
                    name= name,
                    desc = desc
                )
            
            messages.success(request, "Brand Successfully Added")
            return redirect('ecommerce_add_brand')
        return render(request, self.template_name)

class UpdateBrand(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/brands_list.html"

    def post(self, request, brand_id):
        if request.method == "POST":
            requests = Brand.objects.get(id=brand_id)

            name = request.POST.get('name')
            desc = request.POST.get('desc')
            requests.name= name
            requests.desc = desc
            requests.save()
            messages.success(request, "Brand Successfully updated")
            return redirect('ecommerce_add_brand')
        return render(request, self.template_name)

def DeleteBrand(request, brand_id):
        
    brand = get_object_or_404(Brand, pk=brand_id)
    try:
        if brand is not None:
            brand.delete()
            messages.success(request, "Brand Deleted Successfully")
            return redirect("ecommerce_add_brand")
    except:
        messages.error(request, "Error while deletion")
        return redirect("ecommerce_add_brand")
        
    brand = Brand.objects.all()
    
    context = {
        "brands": brand,
    }
    return render(request, "ecommerce/brands_list.html", context = context)


class ProductsAddInventory(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-add-inventory.html"

    def post(self, request):
        if request.method == "POST":

            product_id = request.POST.get('productname')
            product = get_object_or_404(MyProducts, pk=product_id)

            product_qty= request.POST.get('qty')

            previous_qty = product.qty
            qty = int(previous_qty) + int(product_qty)
            
            product.qty = qty
            product.save()

        return render(request, self.template_name)

    def get(self, request):
        products = MyProducts.objects.all()

        context = {
            "products": products
        }
        return render(request, self.template_name, context)

class ProductsAddProduct(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-add-product.html"

    def post(self, request):
        try:
            if request.method == "POST":
                product_name = request.POST.get('productname')

                brand_id = request.POST.get('brand_id')
                brand = get_object_or_404(Brand, pk=brand_id)

                unit_id = request.POST.get('unit_id')
                unit = get_object_or_404(Unit, pk=unit_id)
                
            
                category_id = request.POST['category_id']
                category = get_object_or_404(Category, pk=category_id)

                # product_cost = request.POST.get('cost')
                product_price= request.POST.get('price')
                product_qty= request.POST.get('qty')
                productdesc = request.POST.get('productdesc')
                image = request.FILES.get('image')
                if MyProducts.objects.filter(product_name = product_name).exists():
                    messages.error(request, "Product Already Exists")
                    return redirect('ecommerce-product-list')
                else:
                    MyProducts.objects.create(
                        product_name= product_name,
                        brand = brand,
                        unit = unit,
                        category_id = category,
                        # cost= product_cost,
                        price = product_price,
                        qty=product_qty,
                        product_desc = productdesc,
                        product_image = image

                    )
                    messages.success(request, "Product Added Successfully")
                    return redirect('ecommerce-product-list')

        except:
            
            messages.error(request, "Invalid Form Submission,  Hint: Check for empty form fields, make sure to upload product image")
            return redirect('ecommerce-product-list')
        return render(request, 'ecommerce/product_list.html')
        

    def get(self, request):
        category = Category.objects.all()
        brand = Brand.objects.all()
        unit = Unit.objects.all()
        products = MyProducts.objects.all()
        
        context = {
            "category": category,
            "brands": brand,
            "units": unit,
            "products": products
        }
        return render(request, self.template_name, context)


class UpdateProducts(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-add-product.html"

    def post(self, request,product_id):
        if request.method == "POST":

            requests = MyProducts.objects.get(id=product_id)

            product_name = request.POST.get('productname')

            brand_id = request.POST.get('brand_id')
            brand = get_object_or_404(Brand, pk=brand_id)

            unit_id = request.POST.get('unit_id')
            unit = get_object_or_404(Unit, pk=unit_id)
            
        
            category_id = request.POST['category_id']
            category = get_object_or_404(Category, pk=category_id)

            # product_cost = request.POST.get('cost')
            product_price= request.POST.get('price')
            product_qty= request.POST.get('qty')
            productdesc = request.POST.get('productdesc')
            image = request.FILES.get('image')

            requests.product_name = product_name
            requests.brand = brand
            requests.unit = unit
            requests.category_id = category
            requests.price = product_price
            requests.qty = product_qty
            requests.product_desc = productdesc
            
            if image is not None:
                requests.product_image = image


            requests.save()



        return redirect("ecommerce-product-list")
        

    def get(self, request):
        category = Category.objects.all()
        brand = Brand.objects.all()
        unit = Unit.objects.all()
        products = MyProducts.objects.all()
        
        context = {
            "category": category,
            "brands": brand,
            "units": unit,
            "products": products
        }
        return render(request, self.template_name, context)

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
            
            

        return render(request, 'calendar.html')

        


    def get(self, request):
        event_list = []
        
        sale = EventSale.objects.all()
        events = Event.objects.all()
        
        serialized_event = serialize('json',events)
        
        data = json.loads(serialized_event)
        
        
        for i in data:
            event_list.append(i['fields'])
            
        
        
        event_json = json.dumps(event_list)
        
        context = {
            "events" : event_json,
            "event_sale" : sale
        }
        return render(request, 'calendar.html', {'serialized_events': serialized_event,'event_sale' : sale})
    


class UpdateFoodMenu(LoginRequiredMixin,TemplateView):
    template_name = "items/update_deals.html"
    

    def get(self, request, pk):

        print('i am active get update deals')
        
        food_menu = []
        ammounts = []
        
        
        eventsale = EventSale.objects.filter(id=pk) 
        
        for i in eventsale:
            food_menu.append(i.food_menu)
            ammounts.append(i.no_of_people)
            ammounts.append(i.hall_charges)
        # print(ammounts,'f1')    

        
        # Remove any leading/trailing whitespace and the trailing comma
        cleaned_data = food_menu[0].strip().rstrip(', ')

        # Split the cleaned string into individual items
        items = cleaned_data.split(', ')

        # Initialize an empty dictionary to store the product information
        product_data = {}

        # Iterate through the items and extract product name and quantity
        for item in items:
            name, quantity = map(str.strip, item.split('('))
            quantity = int(quantity.rstrip(')'))
            product_data[name] = quantity

        # Convert the dictionary to JSON
        json_data = json.dumps(product_data)

        print(json_data)
        
        # Parse the JSON data back to a Python dictionary
        product_data = json.loads(json_data)

        # Initialize a dictionary to store product names and their prices
        product_prices = {}

        # Iterate through the product names and retrieve their prices
        for product_name, quantity in product_data.items():
            product = MyProducts.objects.filter(product_name=f"{product_name}").first()
            if product:
                price = product.price
                product_prices[product_name] = {
                    "name": product_name,
                    "quantity": quantity,
                    "price": price
                }
            else:
                # Handle the case where a product is not found
                product_prices[product_name] = {
                    "quantity": quantity,
                    "price": None
                }

        # Convert the product prices to JSON
        json_product_prices = json.dumps(product_prices)

        print(json_product_prices)
        
        products = MyProducts.objects.filter(status=1)
        product_json = []
        for product in products:
            product_json.append({'id': product.id, 'name': product.product_name, 'price': float(product.price)})


        all_products = MyProducts.objects.filter(status=1)
        
    
        
        context = {

                    'products': all_products,
                    'product_json': json_product_prices,
                    'food_menu' : json.dumps(food_menu),
                    'myproducts': json.dumps(product_json),
                    'ammounts' : ammounts,
                    'pk' : pk

                }

            
        return render(request, 'items/update_deals.html' , context)
    
    
    
    def post(self, request, pk):

        # Retrieve JSON data from the POST request
        try:
            # Process and store data as needed
            data = json.loads(request.body)
            
            print(data)
            
            eventsale = EventSale.objects.get(id=pk) 

            extra_charge = eventsale.extra_charges
            entry_charge = eventsale.entry_charges
            stage_charges = eventsale.stage_charges
            
            menu = data["menu"]
            subTotal = data["values"]["subTotal"]
            numberOfPeople = data['values']["numberOfPeople"]
            hallCharges = data["values"]["hallCharges"]
            menuAmount = data["values"]["menuAmount"]
            
            # print(subTotal,numberOfPeople,hallCharges,menuAmount)
            

            eventsale.food_menu = menu
            eventsale.no_of_people = numberOfPeople
            

            per_head = int(hallCharges) + menuAmount
            eventsale.per_head = per_head
            eventsale.total_amount = (int(numberOfPeople) * int(per_head)) + (int(extra_charge) + int(stage_charges) + int(entry_charge)) 
            eventsale.hall_charges = hallCharges
            eventsale.save()
            
            print(menu)
        
            return redirect ("event-sale")
        except json.JSONDecodeError:
            # Handle JSON decoding errors
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)