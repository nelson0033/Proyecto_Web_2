from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('detalle/<id>/',views.vista_detalle, name='vista_detalle'),
]