# Prueba de reproducción del Hito 2

**Integrante:** Marco Garrido
**Fecha:** 22 de octubre de 2026

## 1. Objetivo

El objetivo de esta prueba fue comprobar que el proyecto de análisis de la inflación en Chile pudiera ejecutarse correctamente desde un computador diferente al utilizado durante su desarrollo.

## 2. Procedimiento

Primero, descargué el repositorio del equipo desde GitHub y lo abrí en Visual Studio Code.

Después, instalé Python 3.13 y las librerías necesarias mediante el archivo `requirements.txt`.

También configuré el archivo `.env` con mis credenciales de acceso a las APIs del Banco Central de Chile y FRED.

Finalmente, ejecuté el siguiente comando desde la terminal:

`py -3.13 src/carga_db.py --desde 2015-01-01 --hasta 2026-07-31`

## 3. Resultados

La ejecución terminó correctamente y se obtuvieron los siguientes resultados:

* Se verificó el esquema de la base de datos SQLite.
* Se cargó el catálogo de 12 series económicas.
* Se descargaron correctamente las 12 series desde las APIs oficiales.
* Se cargaron 7.156 observaciones en total.
* No se presentaron errores durante la extracción.

Además, se creó correctamente el archivo `data/coyuntura.db`, que contiene la base de datos SQLite del proyecto.

## 4. Conclusión

La prueba permitió comprobar que el proyecto puede ejecutarse desde otro computador siguiendo las instrucciones de instalación y configuración.

Se consiguieron descargar las 12 series económicas y almacenar las 7.156 observaciones esperadas, sin errores durante el proceso.

Por lo tanto, la prueba de reproducción de la extracción y carga de datos fue exitosa.
