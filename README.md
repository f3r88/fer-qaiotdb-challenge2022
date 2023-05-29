<h1 align="center"> qaiotdb-challenge2022 resolution </h1>

# Configuración del entorno

Este proyecto está desarrollado en Python utilizando el intérprete Anaconda3 y el IDE PyCharm. Las bibliotecas utilizadas en este proyecto son `pytest`, `requests` y `pprint`.

## Instalación de las dependencias

Para instalar las dependencias necesarias para este proyecto, debes tener instalado Python y Anaconda3. Si ya tienes instalado Anaconda3, entonces ya deberías tener Python.

Para instalar las bibliotecas `pytest`, `requests` y `pprint`, puedes usar el comando `pip install` de la siguiente manera:

### `pip install pytest requests pprint`


## Estructura del proyecto

Este proyecto consta de dos archivos principales:

- El archivo `api_consumer.py`, que contiene el código principal de la API.
- El archivo `test_api_consumer.py`, que contiene una suite de pruebas para el código de la API.

## Ejecución de las pruebas

Para ejecutar las pruebas, puedes usar la herramienta `pytest`. Si estás en la misma carpeta que el archivo `test_api_consumer.py`, puedes ejecutar las pruebas con el siguiente comando:


### `pytest test_api_consumer.py `
 

Este comando ejecutará todos los casos de prueba que se encuentren en el archivo `test_api_consumer.py`.

## Conceptos básicos de las pruebas

Las pruebas están diseñadas para verificar que el código de la API funciona como se espera. Cada prueba es un caso de prueba independiente que verifica una funcionalidad específica del código de la API.

Las pruebas utilizan la biblioteca `pytest` para definir y ejecutar los casos de prueba. Cada caso de prueba es una función que comienza con la palabra `test_`, y `pytest` ejecutará automáticamente todas estas funciones cuando se ejecute el comando `pytest`.
