import random
from faker import Faker
from ecommerce.models import EventSale

fake = Faker()

def generate_fake_events(num_events):
    for _ in range(num_events):
        event = EventSale(
            bill_no=None,  # Let the save method handle this
            sr=None,  # Let the save method handle this
            status=random.choice([EventSale.confirm, EventSale.tentative]),
            event_timing=random.choice([EventSale.day, EventSale.night]),
            event_date=fake.date_between(start_date='-30d', end_date='+30d'),
            no_of_people=random.randint(10, 200),
            location="Hall",
            setup=random.choice([EventSale.normal, EventSale.delux, EventSale.vip]),
            deals=fake.sentence(),
            customer_name=fake.name(),
            stage_charges=random.randint(0, 5000),
            entry_charges=random.randint(0, 2000),
            gents=random.randint(0, 150),
            ladies=random.randint(0, 150),
            customer_number=fake.random_int(min=6000000000, max=9999999999),
            per_head=random.randint(50, 200),
            extra_charges=random.randint(0, 1000),
            food_menu=fake.sentence(),
            detials=fake.paragraph(),
            total_menu=random.randint(1, 10),
            payment_details=fake.sentence(),
            payment_count=random.randint(1, 5),
            total_amount=random.randint(5000, 20000),
            recieved_amount=random.randint(500, 10000),
            remaining_amount=0  # Let the save method handle this
        )
        event.save()

if __name__ == '__main__':
    num_fake_events = 20  # Change this to the number of fake events you want to generate
    generate_fake_events(num_fake_events)