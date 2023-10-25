from django.urls import path
from django.views.generic import TemplateView
from ecommerce import views

urlpatterns = [
    # Ecommerce
    
    path('hall-sale-report', views.HallSaleSummary.as_view(),name='hall-sale-report'),
    path('hall-expense-report', views.HallExpenseSummary.as_view(),name='hall-expense-report'),
    
    path('kitchen-sale-report', views.KitchenSaleSummary.as_view(),name='kitchen-sale-report'),
    path('kitchen-expense-report', views.KitchenExpenseSummary.as_view(),name='kitchen-expense-report'),
    
    
    path('ecommerce_product', views.Products.as_view(),name='ecommerce_product'),
    path('ecommerce_product_detail', views.ProductsDetail.as_view(),name='ecommerce_product_detail'),
    path('product-list', views.ProductList.as_view(),name='ecommerce-product-list'),
    path('event-sale', views.Eventsale.as_view(),name='event-sale'),


    
    path('update-event-sale/<int:sale_id>', views.UpdateEventsale.as_view(),name='update-event-sale'),
    path('update-event-expense/<int:expense_id>', views.UpdateEventExpense.as_view(),name='update-event-expense'),
    
    
    
    path('update-product/<int:product_id>', views.UpdateProducts.as_view(),name='update-product'),
    path('delete-product/<int:product_id>/', views.DeleteProducts, name='delete-product'),
    path('delete-sale/<int:sale_id>/', views.delete_sale, name='delete-sale'),
    path('kitchen-sale', views.Kitchensale.as_view(),name='kitchen-sale'),
    path('kitchen-expense', views.Kitchenexpense.as_view(),name='kitchen-expense'),
    path('event-expense', views.Eventexpense.as_view(),name='event-expense'),
    path('ecommerce_add_category', views.ProductsAddCategory.as_view(),name='ecommerce_add_category'),
    path('ecommerce_checkout', views.ProductsCheckout.as_view(),name='ecommerce_checkout'),
    path('ecommerce_shops', views.ProductsShops.as_view(),name='ecommerce_shops'),
    path('ecommerce_add_product', views.ProductsAddProduct.as_view(),name='ecommerce_add_product'),
    path('ecommerce_add_inventory', views.ProductsAddInventory.as_view(),name='ecommerce_add_inventory'),
    path('ecommerce_add_brand', views.ProductsAddBrand.as_view(),name='ecommerce_add_brand'),
    path('ecommerce_add_unit', views.ProductsAddUnit.as_view(),name='ecommerce_add_unit'),


    # path('ecommerce_add_product', views.ProductsAddProduct.as_view(),name='ecommerce_add_product'),
    path('calendar/', views.Calendar.as_view(),name='calendar'),
    path('update_food_menu/<int:pk>', views.UpdateFoodMenu.as_view(), name='update-deals'),
  
    
   
    
]