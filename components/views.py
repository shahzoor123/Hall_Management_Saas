from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
############ Components ############
# UI Elements 
class Alerts(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-alerts.html"
class Buttons(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-buttons.html"
class Cards(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-cards.html"
class Carousel(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-carousel.html"
class Colors(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-colors.html"
class Dropdowns(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-dropdowns.html"
class Generals(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-general.html"
class Grid(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-grid.html"
class Images(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-images.html"
class Lightbox(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-lightbox.html"
class Modals(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-modals.html"
class Progressbars(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-progressbars.html"
class Rangeslider(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-rangeslider.html"
class Rating(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-rating.html"
class SessionTimeout(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-session-timeout.html"
class SweetAlert(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-sweet-alert.html"
class TabsAccordions(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-tabs-accordions.html"
class Typography(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-typography.html"
class Video(LoginRequiredMixin,TemplateView):
    template_name = "components/ui_elements/ui-video.html"

# Forms
class Elements(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-elements.html"
class Validation(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-validation.html"
class Advanced(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-advanced.html"
class Editors(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-editors.html"
class Upload(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-uploads.html"
class Xeditable(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-xeditable.html"
class Wizard(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-wizard.html"
class Mask(LoginRequiredMixin,TemplateView):
    template_name = "components/forms/form-mask.html"

# Charts
class Apex(LoginRequiredMixin,TemplateView):
    template_name = "components/charts/charts-apex.html"
class Chartist(LoginRequiredMixin,TemplateView):
    template_name = "components/charts/charts-chartist.html"
class Chartjs(LoginRequiredMixin,TemplateView):
    template_name = "components/charts/charts-chartjs.html"
class Flot(LoginRequiredMixin,TemplateView):
    template_name = "components/charts/charts-flot.html"
class Knob(LoginRequiredMixin,TemplateView):
    template_name = "components/charts/charts-knob.html"
class Sparkline(LoginRequiredMixin,TemplateView):
    template_name = "components/charts/charts-sparkline.html"

# Tables
class Basic(LoginRequiredMixin,TemplateView):
    template_name = "components/tables/tables-basic.html"
class Datatable(LoginRequiredMixin,TemplateView):
    template_name = "components/tables/tables-datatable.html"
class Editable(LoginRequiredMixin,TemplateView):
    template_name = "components/tables/tables-editable.html"
class Responsive(LoginRequiredMixin,TemplateView):
    template_name = "components/tables/tables-responsive.html"

# Icons
class Dripicons(LoginRequiredMixin,TemplateView):
    template_name = "components/icons/icons-dripicons.html"
class Fontawesome(LoginRequiredMixin,TemplateView):
    template_name = "components/icons/icons-fontawesome.html"
class Materialdesign(LoginRequiredMixin,TemplateView):
    template_name = "components/icons/icons-materialdesign.html"
class Themify(LoginRequiredMixin,TemplateView):
    template_name = "components/icons/icons-themify.html"

# Maps
class Google(LoginRequiredMixin,TemplateView):
    template_name = "components/maps/maps-google.html"
class Vector(LoginRequiredMixin,TemplateView):
    template_name = "components/maps/maps-vector.html"