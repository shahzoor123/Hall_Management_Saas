"""morvin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from layouts import urls
import components
import e_mail
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include
from morvin import views
from django.views.generic import TemplateView
from .views import MyPasswordSetView ,MyPasswordChangeView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    # Index
    path('', views.Index.as_view(),name='index'),
    # Calendar
    path('calendar/', views.Calendar.as_view(),name='calendar'),
    # Chat
    path('chat/', views.Chat.as_view(),name='chat'),
    # Ecommerce
    path('ecommerce/', include('ecommerce.urls')),
    # Email
    path('email/',include('e_mail.urls')),
    # Components
    path('components/', include('components.urls')),
    # Layout
    path('layouts/', include('layouts.urls')),
    # Extras
    path('extras/', include('extras.urls')),
    # Allauth
    path('account/', include('allauth.urls')),
    # logout
    path('logout/', TemplateView.as_view(template_name="account/logout-success.html"),name="logout"),
    #Custum change password done page redirect
    path('accounts/password/change/', login_required(MyPasswordChangeView.as_view()), name="account_change_password"),
    #Custum set password done page redirect
    path('accounts/password/set/', login_required(MyPasswordSetView.as_view()), name="account_set_password"),

]