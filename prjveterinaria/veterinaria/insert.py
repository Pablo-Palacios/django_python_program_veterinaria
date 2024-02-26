import sqlite3


def animal(id, nombre, raza, categoria):
        
        conn = sqlite3.connect("veterinaria.sqlite3")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO animal(id, nombre, raza, categoria)VALUES(?, ?, ?, ?)", (id, nombre, raza, categoria))

        conn.commit()
        conn.close()


#animal(3, "Limon", "mestiso", "Gato")
#animal(4, "Paco", "mestiso", "Perro")


def cliente(dni, nombre, apellido, direccion):
        
        conn = sqlite3.connect("veterinaria.sqlite3")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cliente(num_dni, nombre, apellido, direccion)VALUES(?, ?, ?, ?)", (dni, nombre, apellido, direccion))

        conn.commit()
        conn.close()


cliente(41809969, 'Pablo', 'Palacios', 'Nicefolo Castellanos 5597')
cliente(21628187, 'Marcelo', 'Palacios', 'Mza 34 Casa 7')
cliente(48502641, "Lukas", 'Rodriguez', "Bv Los Alemanes")