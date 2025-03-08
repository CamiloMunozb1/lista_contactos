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
        print("Cierre de base de datos exitosa.")

# Clase para ingresar nuevos contactos
class IngresoContactos:
    def __init__(self, conexion):
        self.conexion = conexion  # Recibe la conexión a la base de datos

    def nuevos_contactos(self):
        """Solicita información al usuario e ingresa un nuevo contacto en la base de datos."""
        try:
            # Solicita los datos del usuario y del nuevo contacto
            nombre_usuario = str(input("Ingresa tu nombre de usuario: ")).strip()
            apellido_usuario = str(input("Ingresa tu apellido de usuario: ")).strip()
            nombre_contacto = str(input("Ingresa el nombre y apellido del contacto: ")).strip()
            numero_contacto = str(input("Ingresa el número telefónico del contacto: ")).strip()
            email_contacto = str(input("Ingresa el email del contacto: ")).strip()

            # Verifica que los campos no estén vacíos
            if not (nombre_usuario and apellido_usuario) or not (nombre_contacto and numero_contacto and email_contacto):
                print("No se permiten campos en blanco.")
                return

            # Busca el ID del usuario en la base de datos
            self.conexion.cursor.execute(
                "SELECT usuario_id FROM usuario_nuevo WHERE nombre_usuario = ? AND apellido_usuario = ?",
                (nombre_usuario, apellido_usuario)
            )
            usuario = self.conexion.cursor.fetchone()

            if usuario:
                usuario_id = usuario[0]
                # Inserta el nuevo contacto en la base de datos
                self.conexion.cursor.execute(
                    "INSERT INTO usuario_contactos (nombre_contacto, numero_contacto, email_contacto, usuario_id) VALUES (?,?,?,?)",
                    (nombre_contacto, numero_contacto, email_contacto, usuario_id)
                )
                self.conexion.conn.commit()
                print(f"Contacto {nombre_contacto}, {numero_contacto}, {email_contacto} ingresado con éxito.")
            else:
                print("Usuario no existe o no se encontró.")

        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            print(f"Error en el programa: {error}.")

# Definición de la ruta de la base de datos y creación de la conexión
ruta_db = "C:/Users/POWER/contactos_lista.db"
conexion = IngresoDB(ruta_db)
