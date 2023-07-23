from django.db import models
from items.models import MyProducts
from items.models import MyProducts, Deals
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

    setup = models.CharField(choices=SETUP_TYPE, default=delux, max_length=10)

    deals = models.ForeignKey(Deals, on_delete=models.PROTECT)

    customer_name = models.CharField(max_length=200)
    customer_number = models.BigIntegerField()
    per_head = models.IntegerField(null=True)
    extra_charges = models.IntegerField()
    food_menu = models.CharField(max_length=200)
    detials = models.TextField()
    total_amount = models.IntegerField(editable=False, null=True)
    recieved_amount = models.IntegerField(null=True)
    remaining_amount = models.IntegerField(editable=False, null=True)

    def __str__(self):
        return str(self.bill_no)

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
    total_expense = models.IntegerField(editable=False, blank=True)

    def __str__(self):
        return str(self.bill)

    def save(self, *args, **kwargs):
        products = MyProducts.objects.filter(code__in=['BBQ', 'WAITERS', 'WATER', 'NAAN', 'DRINKS', 'STUFF'])
        product_dict = {product.code: product for product in products}

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

        # Update the instance with the calculated bbq_price
        self.total_expense = (
            self.pakwan_bill + self.electicity + self.naan_bill + self.cold_drink_bill +
            self.water_bill + self.bbq_price + self.diesel_ltr + self.waiters_bill +
            self.stuff_bill + self.dhobi + self.other_expense + self.setup_bill + self.decor_bill
        )
        super(EventExpense, self).save(*args, **kwargs)



class Event(models.Model):
    event_title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    event_time = models.TimeField()
    # Add any other fields you need for your events


