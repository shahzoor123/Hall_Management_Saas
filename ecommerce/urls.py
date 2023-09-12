from django.urls import path
from django.views.generic import TemplateView
from ecommerce import views
urlpatterns = [
    # Ecommerce
    path('ecommerce_product', views.Products.as_view(),name='ecommerce_product'),
    path('ecommerce_product_detail', views.ProductsDetail.as_view(),name='ecommerce_product_detail'),
    path('event-sale', views.Eventsale.as_view(),name='event-sale'),
    path('update-event-sale/<int:sale_id>', views.UpdateEventsale.as_view(),name='update-event-sale'),
    path('kitchen-sale', views.Kitchensale.as_view(),name='kitchen-sale'),
    path('kitchen-expense', views.Kitchenexpense.as_view(),name='kitchen-expense'),
    path('event-expense', views.Eventexpense.as_view(),name='event-expense'),
    path('ecommerce_add_category', views.ProductsAddCategory.as_view(),name='ecommerce_add_category'),
    path('ecommerce_checkout', views.ProductsCheckout.as_view(),name='ecommerce_checkout'),
    path('ecommerce_shops', views.ProductsShops.as_view(),name='ecommerce_shops'),
    path('ecommerce_add_product', views.ProductsAddProduct.as_view(),name='ecommerce_add_product'),
    # path('ecommerce_add_product', views.ProductsAddProduct.as_view(),name='ecommerce_add_product'),
    path('calendar/', views.Calendar.as_view(),name='calendar'),
]