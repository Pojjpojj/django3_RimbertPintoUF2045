from django.urls import path
from Portfolio import views

urlpatterns = [
    path("galeria/", views.verGaleria,name="galeria"),
]