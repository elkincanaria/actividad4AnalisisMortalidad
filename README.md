# Dashboard de Análisis de Mortalidad en Colombia (2019)
Este proyecto consiste en el desarrollo de una aplicación web interactiva utilizando Dash para visualizar y analizar datos de mortalidad en Colombia durante el año 2019.

## Objetivos Principales:
Proporcionar herramientas visuales para explorar las principales causas de muerte.

Permitir el filtrado por departamento para observar diferencias regionales.

Facilitar la interpretación de los datos mediante gráficos claros e interactivos.

## Componentes Implementados:
Interfaz principal (app.py):

Dropdown para seleccionar departamento.

Siete pestañas con distintos gráficos y tablas:

  Líneas: Muertes por mes.

  Mapa: Distribución geográfica de muertes por departamento.

  Barras: Ciudades con más homicidios.

  Circular: Ciudades con menor mortalidad.

  Tabla: Principales causas de muerte.

  Histograma: Distribución por rango de edad.

  Barras Apiladas: Muertes por sexo y departamento.

## Modularización de callbacks:

Se usan distintos @callback de Dash en archivos independientes dentro de una carpeta callbacks, facilitando la organización y mantenimiento del código.

Cada archivo se importa desde app.py.

## Procesamiento de datos:

Se crea el módulo data_process.py para limpiar y consolidar los datos antes de visualizarlos.

Se aplican filtros condicionales y agrupaciones (groupby) para estructurar los datos según el gráfico deseado, ya sea para Colombia en general o por departamento.

## Visualización geográfica:

Se usa un archivo GeoJSON de https://gist.github.com/john-guerra/43c7656821069d00dcbc con los departamentos de Colombia para generar un mapa coroplético, este se modifica para coincidir con las tablas proporcionadas.

Se ajusta la escala de color para que baja cantidad de muertes se muestren en verde y altas en rojo, utilizando color_continuous_scale=["green", "yellow", "red"].

Control de versiones (Git).
