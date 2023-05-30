from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from items.models import MyProducts
import json

# Create your views here.
class Products(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-products.html"
class ProductsDetail(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-product-detail.html"
class ProductsOrder(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-orders.html"
class ProductsCustomers(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-customers.html"
class ProductsCart(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-cart.html"
class ProductsCheckout(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-checkout.html"
class ProductsShops(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-shops.html"
class ProductsAddProduct(LoginRequiredMixin,TemplateView):
    template_name = "ecommerce/ecommerce-add-product.html"

class Calculate(LoginRequiredMixin,TemplateView):
    template_name = "items/pos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = MyProducts.objects.all()
        product_json = []
        for product in products:
            product_json.append({'id': product.id, 'name': product.name, 'price': float(product.price)})
        context['page_title'] = "Point of Sale"
        context['products'] = products
        context['product_json'] = json.dumps(product_json)
        return context