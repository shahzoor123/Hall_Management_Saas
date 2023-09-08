from django.urls import path
from django.views.generic import TemplateView
from items import views
urlpatterns = [
    # Ecommerce
    path('calculate_menu', views.Calculate.as_view(),name='calculate_menu'),
    path('custom-menu',views.custom_menu,name='custom-menu'),
    path('deals-calculator/<int:deal_id>/', views.item,name='deals-calculator'),


]