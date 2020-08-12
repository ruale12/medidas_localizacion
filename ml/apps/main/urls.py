from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index, name = "home"),
    path('creacion/',views.create, name = "crear"),
    path('modificacion/',views.modify_delete, name = "modificar"),
    path('eliminacion/',views.modify_delete, name = "eliminar"),
]
