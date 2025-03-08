import sqlite3  # Importa la librería para interactuar con SQLite

# Clase para manejar la conexión a la base de datos
class IngresoDB:
    def __init__(self, ruta_db):
        try:
            # Establece conexión con la base de datos SQLite
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            # Maneja errores en la conexión
            print(f"Error en la base de datos: {error}.")

    # Método para cerrar la conexión a la base de datos
    def cierre_base(self):
        self.conn.close()
        print("Cierre de base de datos exitoso.")

# Clase para crear una nueva cuenta de usuario
class NuevaCuenta:
    def __init__(self, conexion):
        self.conexion = conexion  # Recibe la conexión a la base de datos

    def new_cuenta(self):
        try:
            # Solicita el nombre y apellido del usuario
            nombre_usuario = str(input("Ingresa tu nombre de usuario: ")).strip()
            apellido_usuario = str(input("Ingresa tu apellido de usuario: ")).strip()

            # Verifica que los campos no estén vacíos
            if not nombre_usuario or not apellido_usuario:
                print("No se permiten campos en blanco.")
                return

            # Inserta el nuevo usuario en la base de datos
            self.conexion.cursor.execute(
                "INSERT INTO usuario_nuevo (nombre_usuario, apellido_usuario) VALUES (?, ?)",
                (nombre_usuario, apellido_usuario)
            )
            self.conexion.conn.commit()  # Guarda los cambios en la base de datos
            print(f"Usuario {nombre_usuario} {apellido_usuario} ingresado con éxito.")
        
        except ValueError:
            print("Ingresa valores aceptados tipo string.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            print(f"Error en el programa: {error}.")

# Definición de la ruta de la base de datos y creación de la conexión
ruta_db = "C:/Users/POWER/contactos_lista.db"
conexion = IngresoDB(ruta_db)
