from django.urls import path
from layouts import views
urlpatterns = [
    ############### Layout ###############
    # Vertical
    path('layout_darksidebar', views.DarkSidebar.as_view(),name='layout_darksidebar'),
    path('layout_compactsidebar', views.CompactSidebar.as_view(),name='layout_compactsidebar'),
    path('layout_iconsidebar', views.IconSidebar.as_view(),name='layout_iconsidebar'),
    path('layout_boxed', views.Boxed.as_view(),name='layout_boxed'),
    path('layout_preloader', views.Preloader.as_view(),name='layout_preloader'),
    
    # Horizontal
    path('layout_horizontal', views.Horizontal.as_view(),name='layout_horizontal'),
    path('layout_topbarlight', views.TopbarLight.as_view(),name='layout_topbarlight'),
    path('layout_boxedwidth', views.BoxedWidth.as_view(),name='layout_boxedwidth'),
    path('layout_horipreloader', views.HoriPreloader.as_view(),name='layout_horipreloader'),
    path('layout_coloredHeader', views.ColoredHeader.as_view(),name='layout_coloredHeader'),

]