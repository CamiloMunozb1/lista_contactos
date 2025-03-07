from funcion_listados.nueva_cuenta import IngresoDB, NuevaCuenta
from funcion_listados.ingreso_contacto import IngresoDB, IngresoContactos
from funcion_listados.eliminar_contacto import IngresoDB, EliminarContacto
from funcion_listados.mostrar_contactos import IngresoDB, MostarContactos


ruta_db = "C:/Users/POWER/contactos_lista.db"
conexion = IngresoDB(ruta_db)

while True:
    print(
        """
            Bienvenido a su listado de contactos.
            1. Crea una cuenta.
            2. Ingresa el contacto.
            3. Eliminar contactos.
            4. Mostar contactos
            5. Salir.
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
            eliminar_contacto = EliminarContacto(conexion)
            eliminar_contacto.delete_contacto()
        elif usuario == 4:
            mostrar_contactos = MostarContactos(conexion)
            mostrar_contactos.show_contactos()
        elif usuario == 5:
            print("Gracias por usar tu listado de contectos, vuelve pronto.")
            break
        else:
            print("Ingresa un valor adecuado, entre 1-5.")
    except Exception as error:
        print(f"El programa tuvo un error: {error}.")
