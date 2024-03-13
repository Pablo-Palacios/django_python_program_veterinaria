from django.shortcuts import render, redirect
from .forms import DueñosForms, AnimalesForms, TurneroForms
from .models import Dueños, Animales, RegistroConsultas, AdminUsers, TurnosClientes
from django.http import HttpResponse
import sqlite3
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/log")
def index(request, template_name="myapp/index.html"):
   return render(request, template_name)

@login_required(login_url="accounts/login/")
def home(request, template_name="myapp/home.html"):
    return render(request, template_name)

def log(request, template_name="myapp/log.html"):
    return render(request, template_name)

def homeUser(request, template_name="user/homeUser.html"):
    user = request.user
    return render(request, template_name, {'user':user})

def homeAdmi(request, template_name="myapp/admin.html"):
    return render(request, template_name)

def turnos(request, template_name="myapp/turnos.html"):
    return render(request, template_name)

# DUEÑOS

def dueños(request, template_name="myapp/dueños.html"):
    dueños_list = Dueños.objects.all()
    datos = {"dueños":dueños_list}
    return render(request, template_name, datos)



def dueñoForm(request, template_name="myapp/dueño_forms.html"):
    if request.method=="POST":
        forms = DueñosForms(request.POST)
        if forms.is_valid():
            forms.save(commit=True)
            return redirect("hola")
    else:
        forms = DueñosForms()
    datos = {"forms":forms}
    return render(request, template_name, datos)


def modificar_dueño(request, id_pk, template_name="myapp/dueño_forms.html"):
    dueño = Dueños.objects.get(id=id_pk)
    forms = DueñosForms(request.POST or None, instance=dueño)
    if forms.is_valid():
        forms.save(commit=True)
        return redirect("dueños")
    datos={"forms": forms}
    return render(request, template_name, datos)

def eliminar_dueño(request, id_pk, template_name="myapp/eliminar_dato.html"):
    dueño = Dueños.objects.get(id = id_pk)
    if request.method == "POST":
        dueño.delete()
        return redirect("dueños")
    nombre = dueño.nombre
    datos = {"nombre":nombre, "objeto":"el dueño"}
    return render(request, template_name, datos)

# ANIMALES 
 
def animales(request, template_name="myapp/animales.html"):
    animales_list = Animales.objects.all()
    datos = {"animales":animales_list}
    return render(request, template_name, datos)



def formAnimal(request, template_name="myapp/animal_forms.html"):
        if request.method=="POST":
            forms = AnimalesForms(request.POST)
            if forms.is_valid():
                forms.save(commit=True)
                
                fecha = date.today()
                conn = sqlite3.connect('veterinaria.sqlite3')
                cursor = conn.cursor()
                
                cursor.execute("INSERT INTO myapp_registroconsultas (fecha, animal, animal_categoria, tratamiento) VALUES (?, ?, ?, ?)", 
                                (fecha, forms.cleaned_data["nombre"], forms.cleaned_data["categoria"], forms.cleaned_data["tratamiento"]))
                conn.commit()
                cursor.close()
                return redirect("animales")
        else:
            forms = AnimalesForms()
            #dueño = Dueños.objects.all()
        datos = {"forms":forms}
        #dic = {"dueños":dueño}
        return render(request, template_name, datos)


def modificar_animales(request, id_pk, template_name="myapp/animal_forms.html"):
    animal = Animales.objects.get(id = id_pk)
    form = AnimalesForms(request.POST or None, instance=animal)
    if form.is_valid():
        form.save(commit=True)
        return redirect("animales")
    datos = {"form":form}
    return render(request, template_name, datos)

def eliminar_animal(request, id_pk, template_name="myapp/eliminar_dato.html"):
    animal = Animales.objects.get(id=id_pk)
    if request.method =="POST":
        animal.delete()
        return redirect("animales")
    nombre = animal.nombre
    dato = {"nombre":nombre, "objeto":"el animal"}
    return render(request, template_name, dato)


# REGISTRO 
@login_required(redirect_field_name="login")
def registro_consultas(request, template_name="myapp/registros.html"):
    registros = RegistroConsultas.objects.all()
    data = {"registros":registros}
    return render(request, template_name, data)

# ADMIN 
def get_user(request, id,template_name="user/homeUser.html"):
    one_user = User.objects.get(id=id)
    users = {"user":one_user}
    return render(request, template_name, users)

def login_admin(request, template_name="myapp/log.html"):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        
            messages.success(request, "ERROR IN PASSWORD OR USERNAME")
            return redirect("login")
    else:
        return render(request, template_name, {})

#TURNOS 
    
def turnosForms(request, template_name="myapp/turnos.html"):
    form = turnosForms()
    data = {"forms":form}
    return render(request, template_name, data)



"""
def cargar_registro(request, template_name="myapp/registros.html"):
    fecha = time.asctime()
    conn = sqlite3.connect('veterinaria.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT apellido FROM myapp_dueños WHERE ")

    cursor.execute("INSERT INTO myapp_registroconsultas VALUES (null, ?, ?, ?, ?, ?, ?)", )
"""


"""""
def animales(request, template_name='myapp/animales.html'):
    conn = sqlite3.connect('veterinaria.sqlite3')
    animal = conn.cursor()
    animal.execute("SELECT nombre, raza, categoria FROM animal")
    animal_list = animal.fetchall()
    animal.close()

    dato = {"animales": animal_list}
    return render(request, template_name, dato)


def clientes(request, template_name='myapp/clientes.html'):
    conn = sqlite3.connect('veterinaria.sqlite3')
    cliente = conn.cursor()
    cliente.execute("SELECT num_dni, nombre, apellido, direccion FROM cliente")
    cliente_list = cliente.fetchall()
    cliente.close()

    dato = {"clientes": cliente_list}
    return render(request, template_name, dato)


def cliente(request, cliente_dni, template_name='myapp/cliente.html'):
    conn = sqlite3.connect('veterinaria.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT num_dni, nombre, apellido, direccion FROM cliente WHERE num_dni =?", [cliente_dni])
    one_client = cursor.fetchone()
    cursor.close()

    dato = {"cliente": one_client}
    return render(request, template_name, dato)


def animal(request, animal_id, template_name='myapp/animal.html'):
    conn = sqlite3.connect('veterinaria.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, raza, categoria FROM animal WHERE id = ?", [animal_id])
    one_animal = cursor.fetchone()
    cursor.close()

    dato = {"animal": one_animal}
    return render(request, template_name, dato)


def peliculas(request, pelicula, id_comentario, template_name='entidades/Ejercicio2.html'):
    return HttpResponse("pelicula: " + pelicula + "con el comentario: " )


def nuevo_cliente(request, template_name='myapp/clientes_admi.html'):
    if request.method == "POST":
        form = ClienteFrom(request.POST)
        if form.is_valid():
            conn = sqlite3.connect('veterinaria.sqlite3')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cliente VALUES (?, ?, ?, ?)", (form.cleaned_data['dni'], form.cleaned_data['nombre'], form.cleaned_data['apellido'], form.cleaned_data['direccion']))
            conn.commit()
            cursor.close()

            return redirect('clientes')

    else:   
        forms = ClienteFrom()
    datos  = {"forms":forms}
    return render(request, template_name, datos)


def nuevo_animal(request, template_name='myapp/animales_admi.html'):
    if request.method == "POST":
        form = AnimalesForm(request.POST)
        if form.is_valid():
            conn = sqlite3.connect('veterinaria.sqlite3')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO animal VALUES (?, ?, ?, ?, null)", (form.cleaned_data["id"], form.cleaned_data["nombre"], form.cleaned_data["raza"], form.cleaned_data["categoria"]))
            conn.commit()
            cursor.close()

            return redirect('animales')
    else:
        form = AnimalesForm()
    dato = {"forms" : form}
    return render(request, template_name, dato)


"""

