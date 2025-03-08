# Importación de clases desde módulos internos del proyecto
from funcion_listados.nueva_cuenta import IngresoDB, NuevaCuenta
from funcion_listados.ingreso_contacto import IngresoDB, IngresoContactos
from funcion_listados.eliminar_contacto import IngresoDB, EliminarContacto
from funcion_listados.mostrar_contactos import IngresoDB, MostarContactos

# Definición de la ruta de la base de datos y creación de la conexión
ruta_db = "C:/Users/POWER/contactos_lista.db"
conexion = IngresoDB(ruta_db)

# Bucle principal del programa para mostrar el menú de opciones
while True:
    print(
        """
            Bienvenido a su listado de contactos.
            1. Crear una cuenta.
            2. Ingresar un contacto.
            3. Eliminar un contacto.
            4. Mostrar contactos.
            5. Salir.
        """
    )
    
    try:
        # Solicita al usuario que ingrese una opción
        usuario = int(input("Ingresa una opción: "))
        
        # Opción 1: Crear una nueva cuenta
        if usuario == 1:
            new_cuenta = NuevaCuenta(conexion)
            new_cuenta.new_cuenta()
        
        # Opción 2: Ingresar un nuevo contacto
        elif usuario == 2:
            new_contacto = IngresoContactos(conexion)
            new_contacto.nuevos_contactos()
        
        # Opción 3: Eliminar un contacto existente
        elif usuario == 3:
            eliminar_contacto = EliminarContacto(conexion)
            eliminar_contacto.delete_contacto()
        
        # Opción 4: Mostrar la lista de contactos
        elif usuario == 4:
            mostrar_contactos = MostarContactos(conexion)
            mostrar_contactos.show_contactos()
        
        # Opción 5: Salir del programa
        elif usuario == 5:
            print("Gracias por usar tu listado de contactos, vuelve pronto.")
            break
        
        # Manejo de entradas no válidas
        else:
            print("Ingresa un valor adecuado, entre 1-5.")
    
    # Captura y muestra cualquier error inesperado
    except Exception as error:
        print(f"El programa tuvo un error: {error}.")
