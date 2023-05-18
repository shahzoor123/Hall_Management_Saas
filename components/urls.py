from django.urls import path
from components import views
urlpatterns = [
    ############### Components ###############
    # UI Elements
    path('ui_alerts', views.Alerts.as_view(),name='ui_alerts'),
    path('ui_buttons', views.Buttons.as_view(),name='ui_buttons'),
    path('ui_cards', views.Cards.as_view(),name='ui_cards'),
    path('ui_carousel', views.Carousel.as_view(),name='ui_carousel'),
    path('ui_colors', views.Colors.as_view(),name='ui_colors'),
    path('ui_dropdowns', views.Dropdowns.as_view(),name='ui_dropdowns'),
    path('ui_generals', views.Generals.as_view(),name='ui_generals'),
    path('ui_grid', views.Grid.as_view(),name='ui_grid'),
    path('ui_images', views.Images.as_view(),name='ui_images'),
    path('ui_lightbox', views.Lightbox.as_view(),name='ui_lightbox'),
    path('ui_modals', views.Modals.as_view(),name='ui_modals'),
    path('ui_progressbars', views.Progressbars.as_view(),name='ui_progressbars'),
    path('ui_rating', views.Rating.as_view(),name='ui_rating'),
    path('ui_rangeslider', views.Rangeslider.as_view(),name='ui_rangeslider'),
    path('ui_session_timeout', views.SessionTimeout.as_view(),name='ui_session_timeout'),
    path('ui_sweet_alert', views.SweetAlert.as_view(),name='ui_sweet_alert'),
    path('ui_tabs_accordions', views.TabsAccordions.as_view(),name='ui_tabs_accordions'),
    path('ui_typography', views.Typography.as_view(),name='ui_typography'),
    path('ui_video', views.Video.as_view(),name='ui_video'),
    
    # Forms
    path('form_elements', views.Elements.as_view(),name='form_elements'),
    path('form_validation', views.Validation.as_view(),name='form_validation'),
    path('form_advanced', views.Advanced.as_view(),name='form_advanced'),
    path('form_editors', views.Editors.as_view(),name='form_editors'),
    path('form_upload', views.Upload.as_view(),name='form_upload'),
    path('form_xeditable', views.Xeditable.as_view(),name='form_xeditable'),
    path('form_wizard', views.Wizard.as_view(),name='form_wizard'),
    path('form_mask', views.Mask.as_view(),name='form_mask'),

    # Charts
    path('chart_apex', views.Apex.as_view(),name='chart_apex'),
    path('chart_chartist', views.Chartist.as_view(),name='chart_chartist'),
    path('chart_chartjs', views.Chartjs.as_view(),name='chart_chartjs'),
    path('chart_flot', views.Flot.as_view(),name='chart_flot'),
    path('chart_knob', views.Knob.as_view(),name='chart_knob'),
    path('chart_sparkline', views.Sparkline.as_view(),name='chart_sparkline'),

    # Tables
    path('tables_basic', views.Basic.as_view(),name='tables_basic'),
    path('tables_datatable', views.Datatable.as_view(),name='tables_datatable'),
    path('tables_editable', views.Editable.as_view(),name='tables_editable'),
    path('tables_responsive', views.Responsive.as_view(),name='tables_responsive'),

    # Icons
    path('icons_dripicons', views.Dripicons.as_view(),name='icons_dripicons'),
    path('icons_fontawesome', views.Fontawesome.as_view(),name='icons_fontawesome'),
    path('icons_materialdesign', views.Materialdesign.as_view(),name='icons_materialdesign'),
    path('icons_themify', views.Themify.as_view(),name='icons_themify'),

    # Maps
    path('maps_google', views.Google.as_view(),name='maps_google'),
    path('maps_vector', views.Vector.as_view(),name='maps_vector'),

]