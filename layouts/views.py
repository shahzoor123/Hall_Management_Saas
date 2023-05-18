from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
############ Layout ############
# Vertical
class DarkSidebar(LoginRequiredMixin,TemplateView):
    template_name = "layouts/vertical/layouts-dark-sidebar.html"
class CompactSidebar(LoginRequiredMixin,TemplateView):
    template_name = "layouts/vertical/layouts-compact-sidebar.html"
class Boxed(LoginRequiredMixin,TemplateView):
    template_name = "layouts/vertical/layouts-boxed.html"
class IconSidebar(LoginRequiredMixin,TemplateView):
    template_name = "layouts/vertical/layouts-icon-sidebar.html"
class Preloader(LoginRequiredMixin,TemplateView):
    template_name = "layouts/vertical/layouts-preloader.html"
# Horizontal
class Horizontal(LoginRequiredMixin,TemplateView):
    template_name = "layouts/horizontal/layouts-horizontal.html"
class TopbarLight(LoginRequiredMixin,TemplateView):
    template_name = "layouts/horizontal/layouts-hori-topbar-light.html"
class BoxedWidth(LoginRequiredMixin,TemplateView):
    template_name = "layouts/horizontal/layouts-hori-boxed-width.html"
class HoriPreloader(LoginRequiredMixin,TemplateView):
    template_name = "layouts/horizontal/layouts-hori-preloader.html"
class ColoredHeader(LoginRequiredMixin,TemplateView):
    template_name = "layouts/horizontal/layouts-hori-colored-header.html"