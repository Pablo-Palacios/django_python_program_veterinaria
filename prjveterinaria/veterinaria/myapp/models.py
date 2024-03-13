from django.db import models

# Create your models here.

TRATAMIENTO = (
    ("CM", "consulta medica"),
    ("UR", "Urgencia"),
    ("OB", "Observacion regular"),
    ("TQ", "Tratamiento quirurgico"),
    ("SO", "Sin observacines")
    )

ENFERMEDADES = (
    ("Fiebre"),
    ("Mal Estomacal"),
    ("Golpe de calor"), 
    ("Golpe"),
    )


class Dueños(models.Model):
    dni = models.IntegerField("DNI") 
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return  self.apellido + " DNI: " + str(self.dni)

class Animales(models.Model):
    nombre = models.CharField(max_length=20, null=True, blank=True)
    raza = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    dueño = models.ForeignKey(Dueños, on_delete=models.PROTECT)
    tratamiento = models.CharField(max_length=2, choices=TRATAMIENTO, default="SO")
    

    def __str__(self):
        return self.tratamiento



class RegistroConsultas(models.Model):
    fecha = models.DateField()
    dueño = models.IntegerField(null=True, blank=True)
    animal = models.CharField(max_length=20)
    animal_categoria = models.CharField(max_length=20)
    tratamiento = models.CharField(max_length=20)
    

    def __str__(self):
        return self.fecha

class AdminUsers(models.Model):
    userMail = models.EmailField()
    password = models.CharField(max_length=20)
    fullname = models.CharField(null=True, blank=True, max_length=20)


class TurnosClientes(models.Model):
    fecha = models.DateField()
    cliente = models.CharField(max_length=20)
    consulta = models.CharField(max_length=2, choices=TRATAMIENTO, default="SO")
