import sqlite3  # Importa la librería para interactuar con SQLite
import pandas as pd  # Importa pandas para manejar datos tabulares

# Clase para manejar la conexión a la base de datos
class IngresoDB:
    def __init__(self, ruta_db):
        """Inicializa la conexión con la base de datos SQLite."""
        self.conn = sqlite3.connect(ruta_db)
        self.cursor = self.conn.cursor()

    def cierre_base(self):
        """Cierra la conexión con la base de datos."""
        self.conn.close()
        print("Cierre de base de datos exitoso.")

# Clase para mostrar los contactos almacenados
class MostrarContactos:
    def __init__(self, conexion):
        """Recibe la conexión a la base de datos."""
        self.conexion = conexion

    def show_contactos(self):
        """Consulta y muestra los contactos almacenados en la base de datos."""
        try:
            # Consulta SQL para obtener la información de los contactos
            query = """
                SELECT
                    usuario_nuevo.nombre_usuario,
                    usuario_nuevo.apellido_usuario,
                    usuario_contactos.nombre_contacto,
                    usuario_contactos.numero_contacto,
                    usuario_contactos.email_contacto
                FROM usuario_nuevo
                JOIN usuario_contactos 
                ON usuario_nuevo.usuario_id = usuario_contactos.usuario_id
            """
            # Ejecuta la consulta y almacena el resultado en un DataFrame de pandas
            resultado_df = pd.read_sql_query(query, self.conexion.conn)

            # Verifica si hay contactos para mostrar
            if not resultado_df.empty:
                print(resultado_df)
            else:
                print("No se encuentran contactos.")

        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

# Definición de la ruta de la base de datos y creación de la conexión
ruta_db = "C:/Users/POWER/contactos_lista.db"
conexion = IngresoDB(ruta_db)
