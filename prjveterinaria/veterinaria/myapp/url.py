from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"), 
    path("homeUser", views.homeUser, name="homeUser"),
    path("admin", views.homeAdmi, name="admin"),

    # DUEÑOS 
    path("dueños", views.dueños, name="dueños"),
    path("dueñoForms", views.dueñoForm, name="dueñoForms"), 
    path("modificarDueño/<int:id_pk>", views.modificar_dueño, name="modificarDueño"),
    path("eliminarDueño/<int:id_pk>", views.eliminar_dueño, name="eliminarDueño"), 


    # ANIMALES 
    path("animales", views.animales, name="animales"),
    path("animalForms", views.formAnimal, name="animalforms"),
    path("modificarAnimales/<int:id_pk>", views.modificar_animales, name="modificarAnimales"),
    path("eliminarAnimal/<int:id_pk>", views.eliminar_animal, name="eliminarAnimal"),

    # REGISTRO
    path("registros", views.registro_consultas, name="registros"), 

    # LOGIN 
    path("", views.index, name="index"),
    path("log", views.login_admin, name="login")


]
