from django.shortcuts import render , redirect
from items.models import Deals , MyProducts

def deals( request):
    deals = Deals.objects.all()

    context = {
        "deals": deals,
       
    }
    return context
            