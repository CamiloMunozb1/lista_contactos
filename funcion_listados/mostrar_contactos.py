import sqlite3
import pandas as pd

class IngresoDB:
    def __init__(self,ruta_db):
        self.conn = sqlite3.connect(ruta_db)
        self.cursor = self.conn.cursor()

    def cierre_base(self):
        self.conn.close()
        print("Cierre de base de datos exitosa.")


class MostarContactos:
    def __init__(self, conexion):
        self.conexion = conexion

    def show_contactos(self):
        try:
            query = """
                    SELECT
                    usuario_nuevo.nombre_usuario,
                    usuario_nuevo.apellido_usuario,
                    usuario_contactos.nombre_contacto,
                    usuario_contactos.numero_contacto,
                    usuario_contactos.email_contacto
                    FROM usuario_nuevo
                    JOIN usuario_contactos ON usuario_nuevo.usuario_id = usuario_contactos.usuario_id
                    """
            resultado_df = pd.read_sql_query(query,self.conexion.conn)
            if not resultado_df.empty:
                print(resultado_df)
            else:
                print("No se encuentran contactos.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

ruta_db = "C:/Users/POWER/contactos_lista.db"
conexion = IngresoDB(ruta_db)
