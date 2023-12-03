from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('quienesSomos/',views.quienesSomos,name="quienesSomos"),
    path('ubicaciones/',views.ubicaciones,name="ubicaciones"),
    path('departamentos/',views.departamentos,name="departamentos"),
    path('donaciones/',views.donaciones,name="donaciones"),
    path('contacto/',views.contacto,name="contacto")
]
