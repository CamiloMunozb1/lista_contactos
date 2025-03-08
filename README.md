# Gestor de Contactos

Este es un gestor de contactos basado en SQLite que permite a los usuarios crear cuentas, agregar contactos, eliminarlos y visualizar la lista de contactos almacenados en la base de datos.

## Características
- Creación de cuentas de usuario.
- Agregar nuevos contactos asociados a una cuenta.
- Eliminar contactos existentes.
- Mostrar todos los contactos registrados.
- Manejo de excepciones para una experiencia de usuario más robusta.

## Tecnologías utilizadas
- **Python**
- **SQLite**
- **Pandas** (para visualización de datos en tablas)

## Requisitos previos
Antes de ejecutar el proyecto, asegúrate de tener instalado:
- Python 3.x
- Las siguientes bibliotecas (puedes instalarlas con `pip` si no las tienes):
  ```sh
  pip install pandas
  ```

## Estructura del Proyecto
```
contactos_lista/
│── funcion_listados/
│   ├── nueva_cuenta.py
│   ├── ingreso_contacto.py
│   ├── eliminar_contacto.py
│   ├── mostrar_contactos.py
│── contactos.py  # Archivo principal
│── contactos_lista.db  # Base de datos SQLite
│── README.md
```

## Instalación y uso
1. **Clona este repositorio**:
   ```sh
   git clone https://github.com/CamiloMunozb1/contactos_lista.git
   ```
2. **Navega al directorio del proyecto**:
   ```sh
   cd contactos_lista
   ```
3. **Ejecuta el programa**:
   ```sh
   python contactos.py
   ```

## Funcionamiento
Al ejecutar `contactos.py`, verás un menú interactivo con las siguientes opciones:
1. **Crear una cuenta**: Permite registrar un nuevo usuario.
2. **Ingresar un contacto**: Agrega un nuevo contacto asociado a una cuenta.
3. **Eliminar un contacto**: Borra un contacto específico de la base de datos.
4. **Mostrar contactos**: Muestra la lista de contactos almacenados.
5. **Salir**: Cierra el programa.

## Contribución
Si deseas mejorar este proyecto, puedes hacer un **fork** del repositorio y enviar un **pull request** con tus mejoras.

## Autor
Proyecto desarrollado por **Camilo Muñoz**.

## Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

