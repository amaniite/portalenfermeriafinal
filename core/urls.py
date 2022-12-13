from django.urls import path
from django.urls.conf import include
from .views import registroEU, home, registroDatosEU, contacto, search, modificardatos
from . import views

urlpatterns = [
    path("", home, name = "home"),
    path('search', search, name="search"),
    path("contacto/", contacto, name = "contacto"),
    path("registroeu/", registroEU, name = "registroenfermera"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('datoseu/', registroDatosEU, name = "datosenfermera"),
    path('<str:pk>', views.profesionalDetailsView, name='profesional-detalle'),
    path('modificar-eu/<slug:user>', modificardatos, name="modificar_eu"),
]
