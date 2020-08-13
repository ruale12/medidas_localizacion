from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index, name = "home"),
    path('creacion/',views.create, name = "crear"),
    path('modificarlist/',views.modify, name = "modificarlist"),
    path('eliminarlist/',views.delete, name = "eliminarlist"),
    path('modificar/',views.modify_delete, name = "modificar"),
    path('eliminar/',views.modify_delete, name = "eliminar"),
]
