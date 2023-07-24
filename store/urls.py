from django.urls import path
from django.views.generic import TemplateView
from store import views
urlpatterns = [
    # Ecommerce
    path('items', views.Products.as_view(), name='items'),
]