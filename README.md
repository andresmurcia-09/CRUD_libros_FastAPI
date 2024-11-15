# API RESTful para Gestión de Libros

Esta API permite gestionar una colección de libros, permitiendo crear, leer, actualizar y eliminar información sobre ellos. Ha sido desarrollada con FastAPI y utiliza SQLite como base de datos.

## Tabla de Contenidos
1. [Requisitos](#requisitos)
2. [Configuración del Entorno](#configuración-del-entorno)
3. [Instalación](#instalación)
4. [Ejecución](#ejecución)
5. [Documentación de Endpoints](#documentación-de-endpoints)
6. [Pruebas con Postman](#pruebas-con-postman)
7. [Notas adicionales](#notas-adicionales)
------------------------------------------------------------------------

## Requisitos

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Postman

------------------------------------------------------------------------

## Configuración del Entorno

### 1. Crear el Entorno Virtual
Ejecutar el siguiente comando en la raíz del proyecto para crear un entorno virtual:

python -m venv env

### 2. Activar el entorno  virtual

env\Scripts\activate

------------------------------------------------------------------------

## Instalación

### 3. Instalar las dependencias
pip install -r requirements.txt

------------------------------------------------------------------------

## Ejecución

### 3. Iniciar el servidor
uvicorn app:app –reload

------------------------------------------------------------------------

## Documentación de Endpoints

#### 1. Crear un Libro
Método: POST
URL: /libros/
Descripción: Agrega un nuevo libro a la colección.
* Request Body (JSON):
	
{
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "anio_publicacion": 1967,
    "isbn": "978-3-16-148410-0"
}

* Response:

{
    "id": 1,
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "anio_publicacion": 1967,
    "isbn": "978-3-16-148410-0"
}

#### 2. Obtener Todos los Libros
Método: GET
URL: http://127.0.0.1:8000/libros/ 
Descripción: Obtiene la lista de todos los libros.

#### 3. Obtener un Libro por ID
Método: GET
URL: http://127.0.0.1:8000/libros/{id} 
Descripción: Obtiene un libro específico según el ID proporcionado.

#### 4. Actualizar un Libro
Método: PUT
URL: http://127.0.0.1:8000/libros/{id}, (libro por id que quiero actualizar)
Descripción: En body/raw/JSON/ Modifica la información de un libro existente.
SI EL ID NO CORRESPONDE A NINGÚN LIBRO: Libro no encontrado

#### 5. Eliminar un Libro
Método: DELETE
URL: http://127.0.0.1:8000/libros/{id}, (libro por id que quiero eliminar)
Descripción: Elimina un libro de la colección según el ID proporcionado.
SI EL ID NO CORRESPONDE A NINGÚN LIBRO: Libro no encontrado

------------------------------------------------------------------------

## Pruebas con Postman

Para probar esta API, se recomienda el uso de Postman.
1.	Crear un Libro: Usa POST en http://127.0.0.1:8000/libros/ con el body JSON correspondiente.
2.	Obtener Todos los Libros: Usa GET en http://127.0.0.1:8000/libros/.
3.	Obtener un Libro por ID: Usa GET en http://127.0.0.1:8000/libros/{id} (reemplaza {id} por el ID del libro).
4.	Actualizar un Libro: Usa PUT en http://127.0.0.1:8000/libros/{id} con el body JSON de actualización.
5.	Eliminar un Libro: Usa DELETE en http://127.0.0.1:8000/libros/{id}.

------------------------------------------------------------------------

# Notas adicionales
•	Asegurar de que el servidor esté en ejecución antes de realizar pruebas en Postman.
•	La base de datos SQLite se crea automáticamente en el primer arranque del servidor.
