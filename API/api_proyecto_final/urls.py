from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('usuarios',views.UsuarioView.as_view(),name='usuarios'),
    path('usuario/<int:usuario_id>',views.UsuarioDetailView.as_view()),
    path('almacenes',views.AlmacenView.as_view(),name='almacenes'),
    path('almacen/<int:almacen_id>',views.AlmacenDetailView.as_view()),
    path('cargos',views.CargosView.as_view(),name='cargos'),
    path('cargo/<int:cargo_id>',views.CargosDetailView.as_view()),
    path('epps',views.EPPView.as_view(),name='epps'),
    path('epp/<int:epp_id>',views.EPPDetailView.as_view()),
    path('detalles',views.Detalle_almacenView.as_view(),name='detalles'),
    path('detalle/<int:detalle_id>',views.Detalle_almacenDetailView.as_view())
]