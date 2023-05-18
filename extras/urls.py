from django.urls import path
from django.views.generic import TemplateView
from extras import views
urlpatterns = [
    ############### Extras ###############
    # Pages
    path('pages_timeline', views.Timeline.as_view(),name='pages_timeline'),
    path('pages_invoice', views.Invoice.as_view(),name='pages_invoice'),
    path('pages_blank', views.Blankpage.as_view(),name='pages_blank'),
    path('pages_error404', views.Error404.as_view(),name='pages_error404'),
    path('pages_error500', views.Error500.as_view(),name='pages_error500'),
    path('pages_pricing', views.Pricing.as_view(),name='pages_pricing'),
    path('pages_maintenance', views.Maintenance.as_view(),name='pages_maintenance'),
    path('pages_comingsoon', views.Comingsoon.as_view(),name='pages_comingsoon'),
    path('pages_faqs', views.Faqs.as_view(),name='pages_faqs'),
    path('lockscreen', views.Lockscreen.as_view(),name='lockscreen'),
    path('login', views.Login.as_view(),name='login'),
    path('register', views.Register.as_view(),name='register'),

]