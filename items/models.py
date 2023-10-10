from django.db import models
from django.utils import timezone
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name





class Unit(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    unit = models.CharField(max_length=30)
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
            return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class MyProducts(models.Model):
    code = models.CharField(max_length=100, blank=True)
    product_name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    qty = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to = f'product_images/%Y/%m', blank = True)
    product_desc = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now, null=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.product_name

        
class Inventory(models.Model):
    
    product_name = models.ForeignKey(MyProducts, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return f"{self.product_name}"



class Deals(models.Model):
    code = models.CharField(max_length=10, blank=True)
    menu_items = models.ManyToManyField(MyProducts, related_name='deals')
    price_per_head = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.code

    def total_price(self):
        return sum(item.price for item in self.menu_items.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the Deals object first
        self.price_per_head = self.total_price()  # Access the many-to-many relationship after saving
        super().save(*args, **kwargs)  # Save the Deals object again to update the price_per_head field
