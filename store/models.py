from django.db import models

from django.db import models
from django.utils import timezone
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Items(models.Model):
    
    code = models.CharField(max_length=100, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    initial_quantity = models.PositiveIntegerField()
    remaining_quantity = models.PositiveIntegerField()
    def __str__(self):
        return self.name

class Usage(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='item_usages')
    quantity = models.PositiveIntegerField()
    function = models.ForeignKey(settings.ITEM_FUNCTION_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} - {self.quantity} ({self.timestamp})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update the remaining quantity of the item after each usage
        remaining_quantity = self.item.initial_quantity - self.item.item_usages.aggregate(models.Sum('quantity'))['quantity__sum']
        self.item.remaining_quantity = remaining_quantity
        self.item.save()


class FixedResources(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    damage = models.PositiveIntegerField()
    report_date = models.DateTimeField(auto_now_add=True)
