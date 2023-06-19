from django.urls import path
from django.views.generic import TemplateView
from ecommerce import views
urlpatterns = [
    # Ecommerce
    path('calculate_menu', views.Calculate.as_view(),name='calculate_menu'),
    path('deals-calculator', views.DealsCalulator.as_view(),name='deals-calculator'),


]