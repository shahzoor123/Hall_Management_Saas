from django.db import models
from items.models import MyProducts
from items.models import MyProducts, Deals
from django.utils import timezone



class EventSale(models.Model):
    confirm = 'Confirm'
    tentative = 'Tentative '

    STATUS = ((confirm, 'Confirm'),
              (tentative, 'Tentative'),
              )

    day = 'Day'
    night = 'Night '

    EVENT_TIMING = ((day, 'Day'),
                    (night, 'Night'),
                    )

    delux = 'Delux'
    normal = 'Normal'
    vip = 'VIP'

    SETUP_TYPE = ((normal, 'Normal'),
                  (delux, 'Delux'),
                  (vip, 'VIP'),
                  )

    bill_no = models.IntegerField(null=True, unique=True)
    sr = models.IntegerField(null=True)
    status = models.CharField(choices=STATUS, default=tentative, max_length=10)
    event_timing = models.CharField(choices=EVENT_TIMING, default=night, max_length=10)
    booking_date = models.DateField(auto_now_add=True)
    event_date = models.DateField()
    no_of_people = models.IntegerField(null=True)

    location = models.CharField(max_length=10, default="Hall", blank=True)

    setup = models.CharField(choices=SETUP_TYPE, default=delux, max_length=10)

    deals = models.CharField(max_length=200)

    customer_name = models.CharField(max_length=200)
    stage_charges = models.IntegerField(null=True, default=0)
    entry_charges = models.IntegerField(null=True, default=0)

    gents = models.IntegerField(default=0)
    ladies = models.IntegerField(default=0)


    customer_number = models.BigIntegerField()
    per_head = models.IntegerField(null=True)
    extra_charges = models.IntegerField()
    food_menu = models.CharField(max_length=200)
    detials = models.TextField()
    total_menu = models.IntegerField(default=0)
    payment_details = models.TextField()
    payment_count = models.IntegerField(default=0,editable=False)
    total_amount = models.IntegerField(editable=False, null=True)
    recieved_amount = models.IntegerField(null=True)
    remaining_amount = models.IntegerField(editable=False, null=True)

    def __str__(self):
        return str(self.bill_no)

    def save(self, *args, **kwargs):
        # Set payment_details if it's empty
        if not self.payment_details:
            self.payment_count += 1
            self.payment_details = f"{self.payment_count}: Initial Payment was {self.recieved_amount}"

        if not self.bill_no:
            # Get the latest bill_no from the database and increment it
            latest_bill_no = EventSale.objects.aggregate(models.Max('bill_no'))['bill_no__max']
            if latest_bill_no is None:
                latest_bill_no = 0
            self.bill_no = latest_bill_no + 1
        
        # Set sr to be the same as bill_no
        self.sr = self.bill_no
        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.total_amount = (self.no_of_people * self.per_head) + self.extra_charges
    #     self.remaining_amount = self.total_amount - self.recieved_amount
    #     super(EventSale, self).save(*args, **kwargs)


class EventExpense(models.Model):
    bill = models.ForeignKey(EventSale, on_delete=models.PROTECT)
    pakwan_bill = models.IntegerField(default=0, blank=True)
    electicity = models.IntegerField(default=0, blank=True)
    naan_qty = models.IntegerField(default=0, blank=True)
    naan_bill = models.IntegerField(default=0, blank=True, editable=False)
    cold_drink = models.IntegerField(default=0, blank=True)
    cold_drink_bill = models.IntegerField(default=0, blank=True, editable=False)
    water = models.IntegerField(default=0, blank=True)
    water_bill = models.IntegerField(default=0, blank=True, editable=False)
    bbq_kg_qty = models.IntegerField(default=0, blank=True)
    # products = Products.objects.filter(code='BBQ')
    # bbq_product = products.first()
    # bbq_price = bbq_product.price * bbq_kg_qty
    bbq_price = models.IntegerField(default=0, blank=True, editable=False)
    diesel_ltr = models.IntegerField(default=0, blank=True)
    no_of_waiters = models.IntegerField(default=0, blank=True)
    waiters_bill = models.IntegerField(default=0, blank=True, editable=False)
    # add cleaning, soap, etc in html desc. to stuff_bill for clarification
    stuff_bill = models.IntegerField(default=0, blank=True, editable=False)
    # stuff_bill = bill.no_of_people * 24
    dhobi = models.IntegerField(default=0, blank=True)
    other_expense = models.IntegerField(default=0, blank=True)
    other_expense_detals = models.TextField(blank=True)
    setup_bill = models.IntegerField(default=0, blank=True)
    decor = models.CharField(max_length=200, blank=True)
    decor_bill = models.IntegerField(default=0, blank=True)
    total_expense = models.BigIntegerField(editable=False, blank=True)
    expense_date = models.DateField(blank=True)

    
    def save(self, *args, **kwargs):
        # Set the date of the expense to match the date of the sale
        if not self.expense_date:
            self.expense_date = self.bill.event_date
        super(EventExpense, self).save(*args, **kwargs)



    def __str__(self):
        return str(self.bill)

    def save(self, *args, **kwargs):
        products = MyProducts.objects.filter(product_name__in=['BBQ', 'Waiters', 'Water 1.5L', 'Naan', 'Cold Drinks 1.5L', 'STUFF'])
        product_dict = {product.product_name: product for product in products}

        # BBQ PRICE
        bbq_product = product_dict.get('BBQ')
        bbq_price = 0
        if bbq_product is not None:
            bbq_kg_qty = self.bbq_kg_qty
            bbq_price = bbq_product.price * bbq_kg_qty
        self.bbq_price = bbq_price

        # WAITERS PRICE
        waiters_product = product_dict.get('WAITERS')
        waiters_bill = 0
        if waiters_product is not None:
            wait = self.no_of_waiters
            w = waiters_product.price * wait
            waiters_bill = w
        self.waiters_bill = waiters_bill

        # WATER
        water_product = product_dict.get('WATER')
        water_bill = 0
        if water_product is not None:
            water_qty = self.water
            w = water_product.price * water_qty
            water_bill = w
        self.water_bill = water_bill

        # NAAN
        naan_product = product_dict.get('NAAN')
        naan_bill = 0
        if naan_product is not None:
            naan_qty = self.naan_qty
            naan_bill = naan_product.price * naan_qty
        self.naan_bill = naan_bill

        # Cold Drinks
        cold_drink_product = product_dict.get('DRINKS')
        cold_drink_bill = 0
        if cold_drink_product is not None:
            drink_qty = self.cold_drink
            w = cold_drink_product.price * drink_qty
            cold_drink_bill = w
        self.cold_drink_bill = cold_drink_bill

        # Stuffs
        stuff_product = product_dict.get('STUFF')
        stuff_bill = 0
        if stuff_product is not None:
            stuf = self.bill.no_of_people * stuff_product.price
            stuff_bill = stuf
        self.stuff_bill = stuff_bill

    #     # Update the instance with the calculated bbq_price
    #     self.total_expense = (
    #         int(self.pakwan_bill) + int(self.electicity) + int(self.naan_bill) + int(self.cold_drink_bill) +
    #         int(self.water_bill) + int(self.bbq_price) + int(self.diesel_ltr) + int(self.waiters_bill) +
    #         int(self.stuff_bill) + int(self.dhobi) + int(self.other_expense) + int(self.setup_bill) + int(self.decor_bill)
    #     )
    #     super(EventExpense, self).save(*args, **kwargs)


class MyKitchenexpense(models.Model):
    

    bill = models.ForeignKey(EventSale, on_delete=models.PROTECT)
    date = models.DateField()
    payment_details = models.TextField(max_length=300)
    mutton = models.CharField(max_length=50)
    chicken = models.CharField(max_length=50)
    beef = models.CharField(max_length=50)
    rice = models.CharField(max_length=50)
    dahi = models.CharField(max_length=50)
    doodh = models.CharField(max_length=50)
    sabzi = models.CharField(max_length=50)
    fruits = models.CharField(max_length=50)
    khoya_cream_paneer = models.CharField(max_length=50)
    dry_fruits = models.CharField(max_length=50)
    oil = models.CharField(max_length=50)
    other_items_bill = models.CharField(max_length=50)
    other_items_desc = models.CharField(max_length=50)
    total_bill = models.CharField(max_length=50)

    # Define a manager for your model
    objects = models.Manager()

    def __str__(self):
        return str(self.bill)


class Event(models.Model):
    event_title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    event_time = models.CharField(max_length=10)
    # Add any other fields you need for your events


