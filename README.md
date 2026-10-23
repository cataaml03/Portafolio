# Monitor de Coyuntura y Proyección de la Inflación en Chile

**Ciencia de Datos para Economía — Trabajo Semestral**

**Integrantes: Marco Garrido - Catalina Martínez - Gonzalo Mendoza**

## 1. Descripción del proyecto

Este proyecto tiene como finalidad analizar la evolución de la inflación en Chile y realizar una proyección para los próximos 12 meses. Para ello, nos centramos principalmente en cómo se comporta la inflación transable y no transable, y se consideran diversos factores económicos que pueden influir en su evolución.

Los datos utilizados se obtuvieron del Banco Central de Chile y FRED, y se incorporaron variables como el tipo de cambio, el Imacec, la Tasa de Política Monetaria (TPM) y el precio internacional del petróleo.

La pregunta de investigación de nuestro proyecto es:

**¿Cuál será la trayectoria de la inflación en Chile durante los próximos 12 meses y qué factores internos y externos tendrán mayor relación con su evolución, considerando las diferencias entre sus componentes transables y no transables?**

## 2. Objetivo del Hito 2

El Hito 2 consiste en reunir y organizar los datos que necesitamos para desarrollar el proyecto. Para ello, se utilizan las APIs del Banco Central de Chile y FRED, desde donde obtuvimos 12 series económicas.

Después almacenamos la información dentro de una base de datos SQLite para realizar consultas SQL, con el fin de ordenar y trabajar con los datos obtenidos.

Asimismo, realizamos un análisis por medio de Python, en donde elaboramos gráficos para visualizar cómo ha ido evolucionando la inflación y algunas variables que pueden estar relacionadas con su comportamiento. Finalmente, revisamos la calidad de los datos para verificar datos faltantes o posibles errores.

## 3. Fuentes y datos utilizados

Para el desarrollo de nuestro proyecto utilizamos 12 series económicas que fueron obtenidas del Banco Central de Chile y FRED. Las variables seleccionadas nos permiten analizar la inflación de Chile y considerar distintos factores que podrían tener relación con su comportamiento. Las variables utilizadas son:

1. Inflación IPC total interanual.
2. IPC, variación mensual.
3. IPC transables.
4. IPC no transables.
5. IPC sin alimentos y energía (SAE).
6. Tipo de cambio observado (CLP/USD).
7. Tasa de Política Monetaria (TPM).
8. Imacec.
9. Tasa de desempleo nacional.
10. Precio internacional del petróleo Brent.
11. IPC de Estados Unidos.
12. Tasa Fed Funds de Estados Unidos.

## 4. Estructura del repositorio

El repositorio está organizado por medio de carpetas y archivos, entre ellos:

- src/config.py: Contiene la configuración de las 12 series económicas utilizadas.

- src/extraccion.py: Permite descargar datos desde las APIs del Banco Central de Chile y FRED.

- src/carga_db.py: Se encarga de cargar los datos descargados en la base SQLite.

- src/exportar_powerbi.py: Prepara la información para utilizarla en Power BI.

- sql/01_esquema.sql: Contiene la estructura de las tres tablas de la base de datos.

- sql/02_consultas_ejemplo.sql: Incluye las consultas SQL entregadas por el profesor.

- sql/04_consultas_inflacion.sql: Contiene las consultas SQL que se realizaron para el análisis.

- notebooks/01_pipeline_datos.ipynb: Permite revisar el proceso de extracción y carga de datos.

- notebooks/02_analisis_ejemplo.ipynb: Contiene ejemplos de análisis entregados en la plantilla inicial.

- notebooks/03_analisis_coyuntura_inflacion.ipynb: Contiene gráficos, interpretaciones y revisión de calidad de los datos.

- data/coyuntura.db: Almacena los datos económicos descargados. No se sube a GitHub.

- requirements.txt: Contiene las librerías de Python necesarias para ejecutar el proyecto.

- .env.example: Sirve como plantilla para configurar las credenciales de las APIs.

- README.md: Presenta el proyecto y explica cómo reproducir el análisis.

## 5. Reproducción del análisis

Para ejecutar el proyecto desde otro dispositivo, se deben seguir los siguientes pasos:

### Paso 1. Clonar el repositorio

```bash
git clone https://github.com/cataaml03/Portafolio.git
cd Portafolio
```

### Paso 2. Instalar librerías

```bash
py -m pip install -r requirements.txt
```

### Paso 3. Configurar credenciales

Para acceder a las APIs, se debe crear un archivo .env utilizando como referencia el archivo .env.example.

```ini
BCCH_USUARIO=correo_registrado
BCCH_PASSWORD=contraseña
FRED_API_KEY=clave_api
```

Importante: el archivo `.env` contiene credenciales privadas y nunca debe subirse a GitHub.

### Paso 4. Descargar y cargar los datos

Ejecutar desde la carpeta principal del proyecto:

```bash
py src/carga_db.py --desde 2015-01-01 --hasta 2026-07-31
```

Este programa descarga los datos desde las APIs oficiales y genera la base SQLite.

Se debe verificar que las 12 series finalicen con el mensaje [OK].

### Paso 5. Ejecutar el análisis

Abrir en VS Code:
`notebooks/03_analisis_coyuntura_inflacion.ipynb`

Seleccionar un entorno de Python con las dependencias instaladas y ejecutar las celdas en orden.

El notebook utiliza la base SQLite generada en el paso anterior.

## 6. Consultas SQL

Se desarrollaron cuatro consultas específicas para el proyecto:

1. Utilizamos JOIN para relacionar las tablas de nuestra base y así obtener las últimas observaciones disponibles de los indicadores de precios.
2. Utilizamos GROUP BY para calcular el promedio de la inflación interanual de cada año.
3. Utilizamos LAG() para calcular la variación interanual de los componentes transables y no transables del IPC.
4. Utilizamos GROUP BY, AVG y LAG para analizar variaciones interanuales del tipo de cambio y el precio del petroleo.

Las consultas se encuentran en el archivo: sql/04_consultas_inflacion.sql

## 7. Análisis inicial de coyuntura

Luego de haber organizado los datos, se realiza un análisis por medio de Python para observar cómo ha evolucionado la inflación en Chile y algunas variables que pueden tener relación con su comportamiento. Para esto se realizaron 5 gráficos:

1. Inflación total: Muestra la evolución de la inflación interanual en Chile.
2. Inflación transable y no transable: Compara la evolución de ambos componentes del IPC, lo que permite identificar los períodos en los que hay diferencias.
3. Tipo de cambio y precio del petróleo: Muestra cómo se comportan estas 2 variables, las cuales pueden tener relación con los costos y precios de algunos productos.
4. TPM e inflación: Muestra la evolución de la TPM en relación con la inflación.
5. Imacec: Muestra los cambios en la actividad económica.

El análisis y los gráficos se encuentran en: notebooks/03_analisis_coyuntura_inflacion.ipynb.

## 8. Calidad de los datos

Para verificar que la información que descargamos estuviese en buenas condiciones, se realizó una revisión de las 12 series económicas.

En total, se obtuvieron 7.156 observaciones, las cuales corresponden al período de enero de 2015 a julio de 2026. Al revisar los datos pudimos observar que no se encontraron valores nulos ni duplicados para una misma serie y fecha.

Asimismo, revisamos que las series mensuales tuviesen continuidad durante el período analizado. Se verificó que el IPC de Estados Unidos no presenta información para el mes de octubre de 2025. Dicho dato no fue reemplazado ni modificado, dado que preferimos trabajar con la información disponible entregada por las fuentes oficiales.

## 9. Próximas etapas

En las siguientes etapas del proyecto buscamos usar los datos obtenidos para desarrollar modelos capaces de proyectar la inflación en Chile durante los próximos 12 meses.

Para realizar esto, trabajaremos con 2 modelos de proyección, y los resultados obtenidos se compararán para evaluar qué tan bien logran predecir el comportamiento de la inflación.

Asimismo, se espera utilizar Power BI para obtener gráficos que permitan visualizar de manera más simple la evolución de la inflación.

## 10. Alcance del trabajo

Este proyecto tiene fines académicos. Los datos utilizados provienen de fuentes oficiales, en este caso del Banco Central de Chile y FRED. Asimismo, los resultados obtenidos no constituyen pronósticos oficiales ni recomendaciones de política económica.
