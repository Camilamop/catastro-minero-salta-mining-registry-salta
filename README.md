# Catastro Minero de Salta — Análisis de Datos

## Descripción

Proyecto de análisis de datos sobre el catastro minero oficial de la provincia 
de Salta, Argentina. El dataset proviene del Geoportal oficial de la provincia 
y contiene 4.104 registros de concesiones mineras con datos geoespaciales, 
titulares, minerales, estados legales y fechas de inicio.

Este proyecto tiene tres propósitos simultáneos:
- **Investigación para derechos humanos:** insumo analítico para una organización 
  ambiental, con rigor metodológico y trazabilidad de fuentes
- **Proyecto final de Diplomatura en Ciencia de Datos**
- **Portfolio profesional público**

## Pregunta de investigación

¿Cómo se distribuye la propiedad de las concesiones mineras en Salta, 
quiénes son los principales actores y qué redes de relaciones existen 
entre ellos?

## Estructura del repositorio
```
catastro-minero-salta/
├── data/
│   ├── raw/          # Dataset original sin modificar (fuente oficial)
│   └── processed/    # Datos limpios y tablas relacionales
├── notebooks/
│   ├── 01_eda_cleaning.ipynb         # Exploración y limpieza
│   ├── 02_relational_model.ipynb     # Modelado relacional
│   ├── 03_network_analysis.ipynb     # Análisis de redes de actores
│   ├── 04_machine_learning.ipynb     # Clustering y ML
│   └── 05_visualizations.ipynb      # Mapas y visualizaciones
└── src/                              # Funciones reutilizables
```

## Stack tecnológico

| Área | Herramientas |
|---|---|
| Procesamiento de datos | Python, pandas, geopandas |
| Análisis geoespacial | geopandas, folium, plotly |
| Análisis de redes | NetworkX |
| Machine learning | scikit-learn |
| Base de datos | PostgreSQL + PostGIS |
| Visualización | Power BI / Tableau |

## Fuente de datos

- **Organismo:** Secretaría de Minería de la Provincia de Salta
- **URL:** https://geoportal.salta.gob.ar/catalogue/uuid/72c41757-bdee-4215-ab4e-9a02fc56954e
- **Formato:** Shapefile (MULTIPOLYGON, WGS84)
- **Registros:** 4.104 concesiones mineras
- **Última actualización del dataset:** Diciembre 2025
## Consideraciones éticas

El dataset es de carácter público oficial. El análisis incluye datos de 
personas físicas que, si bien son públicos en su rol de concesionarios 
mineros registrados, son tratados con las consideraciones éticas propias 
de la investigación en derechos humanos.

## Autora

Camila Agustina Mopty  
Diplomatura en Ciencia de Datos en R y Python en Instituto Data Science Argentina 
Linkedin: www.linkedin.com/in/camila-mopty · mail: camilamopty@gmail.com