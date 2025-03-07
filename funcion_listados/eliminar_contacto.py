import sqlite3

class IngresoDB:
    def __init__(self, ruta_db):
        try:
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

    def cierre_base(self):
        self.conn.close()
        print("Cierre de base de datos exitosa.")

class EliminarContacto:
    def __init__(self,conexion):
        self.conexion = conexion

    def delete_contacto(self):
        try:
            nombre_usuario = str(input("Ingresa tu nombre de usuario: ")).strip()
            apellido_usuario = str(input("Ingresa tu apellido de usuario: ")).strip()
            nombre_contacto = str(input("Ingresa el nombre y apellido del contacto a eliminar: ")).strip()
            if not (nombre_usuario and apellido_usuario) or not nombre_contacto:
                print("No se permiten campos en blanco.")
                return
            self.conexion.cursor.execute("SELECT usuario_id FROM usuario_nuevo WHERE nombre_usuario = ? AND apellido_usuario = ?",(nombre_usuario,apellido_usuario))
            usuario = self.conexion.cursor.fetchone()
            if usuario:
                usuario_id = usuario[0]
                self.conexion.cursor.execute("DELETE FROM usuario_contactos WHERE nombre_contacto = ? AND usuario_id = ?",(nombre_contacto,usuario_id))
                self.conexion.conn.commit()
                print("Contacto eliminado.")
            else:
                ("Usuario no existe o no es encontrado.")
        except ValueError:
            print("Ingresa valores tipo string.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            print(f"Error en el programa: {error}.")


ruta_db = "C:/Users/POWER/contactos_lista.db"
conxion = IngresoDB(ruta_db)
        