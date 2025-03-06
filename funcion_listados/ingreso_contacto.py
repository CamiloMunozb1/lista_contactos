import sqlite3

class IngresoDB:
    def __init__(self,ruta_db):
        try:
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

    def cierre_base(self):
        self.conn.close()
        print("Cierre de base de datos exitosa.")


class IngresoContactos:
    def __init__(self,conexion):
        self.conexion = conexion

    def nuevos_contactos(self):
        nombre_usuario = str(input("Ingresa tu nombre de usuario: "))
        apellido_usuario = str(input("Ingresa tu apellido de usuario: "))
        nombre_contacto = str(input("Ingresa el nombre y apellido del contacto: ")).strip()
        numero_contacto = str(input("Ingresa el numero telefonico del contacto: ")).strip()
        email_contacto = str(input("Ingresa el email del contacto: ")).strip()
        if not nombre_contacto or not numero_contacto and email_contacto:
            print("No se permiten campos en blanco.")
            return
        self.conexion.cursor.execute("SELECT usuario_id FROM usuario_nuevo WHERE nombre_usuario = ? AND apellido_usuario = ?",(nombre_usuario,apellido_usuario))
        usuario = self.conexion.cursor.fetchone()
        if usuario:
            usuario_id = usuario[0]
            self.conexion.cursor.execute("INSERT INTO usuario_contactos (nombre_contacto, numero_contacto, email_contacto, usuario_id) VALUES (?,?,?,?)",(nombre_contacto,numero_contacto,email_contacto,usuario_id))
            self.conexion.conn.commit()
            print(f"Contacto {nombre_contacto}, {numero_contacto}, {email_contacto} ingresado.")
        else:
            print("Usuario no existe o no es encontrado.")



ruta_db = "C:/Users/POWER/contactos_lista.db"
conexion = IngresoDB(ruta_db)