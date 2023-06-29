from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MyProducts(models.Model):
    
    code = models.CharField(max_length=100, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.code + " - " + self.name


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


    
