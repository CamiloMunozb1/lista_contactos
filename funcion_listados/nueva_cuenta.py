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

class NuevaCuenta:
    def __init__(self,conexion):
        self.conexion = conexion

    def new_cuenta(self):
        try:
            nombre_usuario = str(input("Ingresa tu nombre de usuario: ")).strip()
            apellido_usuario = str(input("Ingresa tu apellido de usuario: ")).strip()
            if not nombre_usuario or not apellido_usuario:
                print("No se permiten campos en blanco.")
                return
            self.conexion.cursor.execute("INSERT INTO usuario_nuevo (nombre_usuario,apellido_usuario) VALUES (?,?)",(nombre_usuario,apellido_usuario))
            self.conexion.conn.commit()
            print(f"Usuario {nombre_usuario} {apellido_usuario} ingresado.")
        except ValueError:
            print("Ingresa valores acetados tipo string.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            print(f"Error en el programa: {error}.")


ruta_db = "C:/Users/POWER/contactos_lista.db"
conexion = IngresoDB(ruta_db)