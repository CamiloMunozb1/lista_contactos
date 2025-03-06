from funcion_listados.nueva_cuenta import IngresoDB, NuevaCuenta
from funcion_listados.ingreso_contacto import IngresoDB, IngresoContactos


ruta_db = "C:/Users/POWER/contactos_lista.db"
conexion = IngresoDB(ruta_db)

while True:
    print(
        """
            Bienvenido a su listado de contactos.
            1. Crea una cuenta.
            2. Ingresa el contacto.
            4. Eliminar contactos.
            5. Mostar contactos
            6. Salir.
        """
        )
    try:
        usuario = int(input("Ingresa una opcion: "))
        if usuario == 1:
            new_cuenta = NuevaCuenta(conexion)
            new_cuenta.new_cuenta()
        elif usuario == 2:
            new_contacto = IngresoContactos(conexion)
            new_contacto.nuevos_contactos()
        elif usuario == 3:
            print("Proxima funcion.")
        elif usuario == 4:
            print("Proxima funcion.")
        elif usuario == 5:
            print("Proxima funcion.")
        elif usuario == 6:
            print("Gracias por usar tu listado de contectos, vuelve pronto.")
            break
        else:
            print("Ingresa un valor adecuado, entre 1-4")
    except Exception as error:
        print(f"El programa tuvo un error: {error}.")
