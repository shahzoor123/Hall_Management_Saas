from django.db import models
from items.models import MyProducts

class EventSale(models.Model):
    confirm = 'Confirm'
    tentative = 'Tentative '

    STATUS = ((confirm, 'Confirm'),
              (tentative, 'Tentative '),
              )

    day = 'Day'
    night = 'Night '

    EVENT_TIMING = ((day, 'Day'),
                    (night, 'Night '),
                    )

    delux = 'Delux'
    normal = 'Normal'
    vip = 'VIP'

    SETUP_TYPE = ((normal, 'Normal'),
                  (delux, 'Delux '),
                  (vip, 'VIP '),
                  )

    bill_no = models.IntegerField(default=000)
    sr = models.IntegerField(default=000)
    status = models.CharField(choices=STATUS, default=tentative, max_length=10)
    event_timing = models.CharField(choices=EVENT_TIMING, default=night, max_length=10)
    booking_date = models.DateField(auto_now_add=True)
    event_date = models.DateField(blank=True)
    no_of_people = models.IntegerField(default=0)
    setup = models.CharField(choices=SETUP_TYPE, default=delux, max_length=10)
    customer_name = models.CharField(max_length=200)
    customer_number = models.BigIntegerField(blank=True)
    per_head = models.IntegerField(default=000)
    extra_charges = models.IntegerField(blank=True)
    food_menu = models.CharField(blank=True, max_length=200)
    detials = models.TextField(blank=True)
    total_amount = models.IntegerField(blank=True, editable=False)
    recieved_amount = models.IntegerField(blank=True)
    remaining_amount = models.IntegerField(blank=True, editable=False)

    def __str__(self):
        return str(self.bill_no)

    def save(self, *args, **kwargs):
        self.total_amount = (self.no_of_people * self.per_head) + self.extra_charges
        self.remaining_amount = self.total_amount - self.recieved_amount
        super(EventSale, self).save(*args, **kwargs)


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
        # BBQ PRICE
        products = Products.objects.filter(code='BBQ')
        bbq_product = products.first()

        if bbq_product is not None:
            bbq_kg_qty = self.bbq_kg_qty
            bbq_price = bbq_product.price * bbq_kg_qty
        self.bbq_price = bbq_price


        # WAITERS PRICE
        waiter = Products.objects.filter(code='WAITERS')
        waiters = waiter.first()

        if waiters is not None:
            wait = self.no_of_waiters
            w = waiters.price * wait
        self.waiters_bill = w

        # WATER
        water = Products.objects.filter(code='WATER')
        wat = water.first()

        if wat is not None:
            water_qty = self.water
            w = wat.price * water_qty
        self.water_bill = w


        # NAAN
        naans = Products.objects.filter(code='NAAN')
        naan = naans.first()
        if naan is not None:
            nan_qty = self.naan_qty
            naan = naan.price * nan_qty
        self.naan_bill = naan

        # Cold Drinks
        drinks = Products.objects.filter(code='DRINKS')
        cold_drink = drinks.first()
        if cold_drink is not None:
            drink_qty = self.cold_drink
            drink = cold_drink.price * drink_qty
        self.cold_drink_bill = drink

        # Stuffs
        stuff = Products.objects.filter(code='STUFF')
        st = stuff.first()
        if st is not None:
            stuf = self.bill.no_of_people * st.price
        self.stuff_bill = stuf

        # Update the instance with the calculated bbq_price
        EventExpense.objects.filter(id=self.id).update(bbq_price=bbq_price)
        self.total_expense = self.pakwan_bill + self.electicity + self.naan_bill + self.cold_drink_bill + self.water_bill + self.bbq_price + self.diesel_ltr + self.waiters_bill + self.stuff_bill + self.dhobi + self.other_expense + self.setup_bill + self.decor_bill
        super(EventExpense, self).save(*args, **kwargs)
  
    